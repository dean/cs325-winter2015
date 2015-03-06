from pulp import *

prob = LpProblem("The Bicycle Problem", LpMinimize)
t10 = LpVariable("t10",0)
t20 = LpVariable("t20",0)
t30 = LpVariable("t30",0)
prob += t10+t20+t30
prob += 3*t30+2*t20+t10 >= 540
prob += 17*t30+10*t20+3*t10 <= 2000
status = prob.solve()
print LpStatus[status]
print value(prob.objective)
print value(t10)
print value(t20)
print value(t30)
