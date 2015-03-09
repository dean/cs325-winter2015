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
t = LpVariable("t")
prob += t

def T(day):
    global prob, x0, x1, x2, x3, x4, x5
    return (x0 +
            x1*day +
            x2*math.cos((2*math.pi*day)/365.25) +
            x3*math.sin((2*math.pi*day)/365.25) +
            x4*math.cos((2*math.pi*day)/(365.25 * 10.7)) +
            x5*math.sin((2*math.pi*day)/(365.25 * 10.7)))

def main():
    global prob, x0, x1, x2, x3, x4, x5
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = reader.next()
        rows = list(reader)

        for row in reader:
            avg, day = int(row[-2]), int(row[-1])
            prob += avg - T(day) <= t
            prob += avg - T(day) <= -t
            # prob += T(int(row[-1]))

        status = prob.solve()
        print LpStatus[status]
        print value(prob.objective)
        print value(x0)
        print value(x1)
        print value(x2)
        print value(x3)
        print value(x4)
        print value(x5)
        print t



if len(sys.argv) < 2:
    exit('Please provide an input file.')
main()




