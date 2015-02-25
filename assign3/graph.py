import sys

import matplotlib
from scipy import stats
matplotlib.use('ps')

import numpy as np
import matplotlib.pyplot as plt


def make_graph(vals):
    xs = vals[0]
    alg = vals[1]
    plt.plot(xs, alg, color='green')
    plt.suptitle('Closest to Zero')
    plt.xlabel('Input Size (Size of Array)')
    plt.ylabel('Average Runtime (100 Runs) in milliseconds')

    plt.savefig('timings.ps')

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Use --graph or --slope'

    f = filter(lambda x: x, open('timings.txt', 'r').read().split('\n')[1:])
    f = map(lambda x: filter(lambda y: y, x.split(' ')), f)
    vals = map(lambda x: (x[0], float(x[1]) * 1000), f)  # Pull out float and convert to milliseconds
    new_vals = [[], []]

    if sys.argv[1] == '--graph':
        for val_list in vals:
            for j, thing in enumerate(val_list):
                new_vals[j % 2].append(thing)

        make_graph(new_vals)

    if sys.argv[1] == '--slope':
        for val_list in vals:
            for j, thing in enumerate(val_list):
                new_vals[j % 2].append(thing)

        slope, intercept = np.polyfit(np.log(new_vals[0]), np.log(new_vals[1]), 1)
        print 'Slope: {0} Intercept: {1}'.format(slope, intercept)
