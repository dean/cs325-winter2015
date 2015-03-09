import csv
import math

from pulp import *


prob = LpProblem("Local Temperature Change", LpMinimize)
x0 = LpVariable("x0", 0)
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)
z = LpVariable("z")
prob += z
prob += z >= 0

def T(day):
    global prob, x0, x1, x2, x3, x4, x5
    return (
        (x5*math.sin((2*math.pi*day)/(365.25 * 10.7))) +
        (x4*math.cos((2*math.pi*day)/(365.25 * 10.7))) +
        (x3*math.sin((2*math.pi*day)/365.25)) +
        (x2*math.cos((2*math.pi*day)/365.25)) +
        (x1*day) +
        x0
    )


def main():
    global prob, x0, x1, x2, x3, x4, x5
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = reader.next()
        rows = list(reader)

        for row in rows:
            avg, day = float(row[-2]), float(row[-1])
            prob += z >= (avg - T(day))
            prob += z >= -(avg - T(day))

        status = prob.solve()
        print "Status %s" % LpStatus[status]
        print "Objective %s" % prob.objective
        print "Objective (value) %s" % value(prob.objective)
        print "Values:"
        print value(x0)
        print value(x1)
        print value(x2)
        print value(x3)
        print value(x4)
        print value(x5)
        print value(z)


if len(sys.argv) < 2:
    exit('Please provide an input file.')
main()




