import matplotlib.pyplot as plt
from pylab import *


def make_graph(vals):
    xs = vals[0]
    alg1, alg2, alg3 = vals[1:]
    f, subplots = plt.subplots(2, 1, sharex='row')
    subplots[0].plot(xs[:9], alg1[:9], color='blue')
    subplots[0].plot(xs, alg2, color='green')
    subplots[0].plot(xs, alg3, color='red')
    subplots[1].loglog(xs[:10], alg1[:10], color='blue')
    subplots[1].plot(xs, alg2, color='green')
    subplots[1].plot(xs, alg3, color='red')

    # ax = fig.add_subplot(1,1,1)
    # bx = fig.add_subplot(2,1,1)

    # for val in vals:
    #   line = ax.plot(*val, color='blue', lw=2)
        # line = bx.plot(*val, color='red', lw=2)
    # line2 = bx.plot(

    # ax.set_yscale('log')
    # ax.set_xscale('log')

    # for val in vals:
    #     ax.plot(*val)
    #     print val
    plt.savefig('timings.pdf')

if __name__ == '__main__':
    vals = map(lambda x: map(lambda z: float(z.strip()), filter(lambda y: y, x.split(' '))), open('timings.txt', 'r').readlines()[1:])
    new_vals = [[], [], [], []]
    for val_list in vals:
        for j, thing in enumerate(val_list):
            new_vals[j % 4].append(thing)

    make_graph(new_vals)
