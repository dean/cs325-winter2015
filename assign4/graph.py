import sys

import matplotlib
matplotlib.use('ps')

import matplotlib.pyplot as plt
import assignment4


def make_graph(days, avg, computed_avg, linear_y, outputfile='timings.ps'):
    plt.scatter(days, avg, color='blue', facecolor='0.5', lw=0.5, s=1)
    plt.plot(days, computed_avg, color='red')
    plt.plot(days, linear_y, color='green')
    plt.suptitle('Avg Temperature for Corvallis')
    plt.xlabel('Days')
    plt.ylabel('Avg Temp')

    plt.savefig(outputfile)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print 'Provide input data.'
        exit(0)

    outputfile = 'timings.ps'
    if len(sys.argv) > 2:
        outputfile = sys.argv[2]

    rows = assignment4.process_file(sys.argv[1])
    days, avgs = [], []
    for row in rows:
        avg, day = row
        avgs.append(avg)
        days.append(day)

    _, _, lp_x_values = assignment4.solve(rows)

    computed_avgs = [assignment4.t(d, *lp_x_values) for d in days]
    linear_y = [assignment4.linear_part(d, *lp_x_values[:2]) for d in days]

    make_graph(days, avgs, computed_avgs, linear_y, outputfile=outputfile)
