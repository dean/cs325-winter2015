import csv
import math
import sys

import matplotlib
from scipy import stats
matplotlib.use('ps')

import numpy as np
import matplotlib.pyplot as plt

x0 = 7.5576517
x1 = 0.00023193911
x2 = 4.9302622
x3 = 8.4965903
x4 = 0.0
x5 = 0.0

def make_graph(x1s, y1s, x2s, y2s):
    plt.plot(x1s, y1s, color='blue')
    plt.plot(x2s, y2s, color='red')
    plt.suptitle('Avg Temperature for Corvallis')
    plt.xlabel('Days')
    plt.ylabel('Avg Temp')

    plt.savefig('timings.ps')


def get_original_data_points():
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = reader.next()
        rows = list(reader)

        avgs, days = [], []
        for row in rows:
            avgs.append(float(row[-2]))
            days.append(float(row[-1]))
        return days, avgs


def T(day):
    global x0, x1, x2, x3, x4, x5
    return (
        (x5*math.sin((2*math.pi*day)/(365.25 * 10.7))) +
        (x4*math.cos((2*math.pi*day)/(365.25 * 10.7))) +
        (x3*math.sin((2*math.pi*day)/365.25)) +
        (x2*math.cos((2*math.pi*day)/365.25)) +
        (x1*day) +
        x0
    )

def get_calculated_data_points():
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = reader.next()
        rows = list(reader)

        avgs, days = [], []
        for row in rows:
            day = float(row[-1])
            avgs.append(T(day))
            days.append(day)
        return days, avgs


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Provide input data.'
        exit(0)
    x1s, y1s = get_original_data_points()
    x2s, y2s = get_calculated_data_points()
    make_graph(x1s, y1s, x2s, y2s)
