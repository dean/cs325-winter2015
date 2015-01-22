import sys

import matplotlib
from scipy import stats
matplotlib.use('ps')

import numpy as np
import matplotlib.pyplot as plt


def make_graph(vals):
    xs = vals[0]
    alg1, alg2, alg3 = vals[1:]
    f, subplots = plt.subplots(2, 1, sharex='row')
    f.set_tight_layout(True)
    f.subplots_adjust(hspace=2.25)
    plt.suptitle('Max Subarray Experimental Runtime Analysis')
    subplots[0].set_title('Linear Axes')
    subplots[0].plot(xs[:9], alg1[:9], color='blue')
    subplots[0].plot(xs, alg2, color='green')
    subplots[0].plot(xs, alg3, color='red')
    subplots[0].set_xlabel('Input Size')
    subplots[0].set_ylabel('Average Runtime (10 Runs)')
    subplots[1].set_title('Logarithmic Axes')
    subplots[1].loglog(xs[:10], alg1[:10], color='blue')
    subplots[1].plot(xs, alg2, color='green')
    subplots[1].plot(xs, alg3, color='red')
    subplots[1].set_ylabel('Average Runtime (10 Runs)')
    subplots[1].set_xlabel('Input Size')

    plt.savefig('timings.ps')

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Use --graph or --slope'

    vals = map(lambda x: map(lambda z: float(z.strip()), filter(lambda y: y, x.split(' '))), open('timings.txt', 'r').readlines()[1:])
    new_vals = [[], [], [], []]

    if sys.argv[1] == '--graph':
        for val_list in vals:
            for j, thing in enumerate(val_list):
                new_vals[j % 4].append(thing)

        make_graph(new_vals)

    if sys.argv[1] == '--slope':
        for val_list in vals:
            for j, thing in enumerate(val_list):
                new_vals[j % 4].append(thing)

        slope, intercept = np.polyfit(np.log(new_vals[0][:9]), np.log(new_vals[1][:9]), 1)
        print 'Alg1 Slope: {0} Intercept: {1}'.format(slope, intercept)
        for i in range(2):
            slope, intercept = np.polyfit(np.log(new_vals[0]), np.log(new_vals[2+i]), 1)
            print 'Alg{0} Slope: {1} Intercept: {2}'.format(i + 2, slope, intercept)

