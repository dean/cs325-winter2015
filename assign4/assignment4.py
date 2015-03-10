import csv
import math

from pulp import *


def t(day, x0, x1, x2, x3, x4, x5):
    return (
        (x5 * math.sin((2 * math.pi * day) / (365.25 * 10.7))) +
        (x4 * math.cos((2 * math.pi * day) / (365.25 * 10.7))) +
        (x3 * math.sin((2 * math.pi * day) / 365.25)) +
        (x2 * math.cos((2 * math.pi * day) / 365.25)) +
        (x1 * day) +
        x0
    )


def get_differences(rows, xs):
    diffs = []
    for row in rows:
        avg, day = row
        diffs.append(avg - t(day, *xs))
    return diffs


def solve(rows):
    prob = LpProblem("Local Temperature Change", LpMinimize)
    z = LpVariable("z")
    xs = [LpVariable("x%d" % i, 0) for i in xrange(6)]

    prob += z
    prob += z >= 0

    diffs = get_differences(rows, xs)
    for diff in diffs:
        # print diff
        # print -diff
        # return
        prob += (z >= diff)
        prob += (z >= -diff)

    status = prob.solve()
    return LpStatus[status], map(value, xs)


def process_file(f):
    rows = []
    with open(f, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # Skip the header
        reader.next()
        for row in reader:
            rows.append(map(float, row[-2:]))
    return rows


def main(args):
    rows = process_file(args[0])
    status, lp_x_values = solve(rows)

    print "Status %s" % status
    print "Values:"
    for i in xrange(6):
        print "x%d value: %s" % (i, lp_x_values[i])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit('Please provide an input file.')
    main(sys.argv[1:])
