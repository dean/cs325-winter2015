import sys

import matplotlib
matplotlib.use('ps')

import matplotlib.pyplot as plt
import assignment4


def make_graph(x1s, y1s, x2s, y2s):
    plt.plot(x1s, y1s, color='blue')
    plt.plot(x2s, y2s, color='red')
    plt.suptitle('Avg Temperature for Corvallis')
    plt.xlabel('Days')
    plt.ylabel('Avg Temp')

    plt.savefig('timings.ps')


def get_calculated_data_points(days, lp_x_values):
    return [assignment4.t(day, *lp_x_values) for day in days]


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print 'Provide input data.'
        exit(0)

    rows = assignment4.process_file(sys.argv[1])
    days, avgs = [], []
    for row in rows:
        avg, day = row
        avgs.append(avg)
        days.append(day)

    _, lp_x_values = assignment4.solve(rows)

    computed_avgs = list(get_calculated_data_points(days, lp_x_values))

    make_graph(days, avgs, days, computed_avgs)
