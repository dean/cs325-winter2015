import random
import time
import urllib2
import sys


def alg1(arr):
    pass

def alg2(arr):
    pass

def alg3(arr):
    pass

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Usage: python assignment1.py [option]'
        print 'Options:'
        options = ['--test', '--time', '--solve']
        print '\n'.join(map(lambda x:'\t'+ x, options))
        sys.exit()
    elif sys.argv[1] == '--test':
        test_set_url = 'http://web.engr.oregonstate.edu/~glencora/cs325/mstest.txt'
        test_sets = urllib2.urlopen(test_set_url).read().strip()
        for test_set in test_sets.split('\n'):
            arr, ans = eval(test_set)
            # Test here

    elif sys.argv[1] == '--time':
        random.seed(931915823)
        print 'Size |   Alg 1   |   Alg2   |   Alg3   '
        timing_format = '{:<5} {:^11} {:^11} {:^11}'
        for size in xrange(100, 1001, 100):
            arr = [random.randint(0, 100) for x in xrange(size)]
            timing = []
            for alg in [alg1, alg2, alg3]:
                start = time.clock()
                alg(arr)
                timing.append(time.clock() - start)
            timing = [size] + timing
            print timing_format.format(*timing)

        for size in xrange(2000, 9001, 1000):
            arr = [random.randint(0, 100) for x in xrange(size)]
            lines = sorted(map(lambda x: Line(*x), zip(ms, bs)), key=lambda x: x.m)
            timing = []
            start = time.clock()
            alg(lines)
            timing.append(time.clock() - start)
            timing = [size, '', ''] + timing + [0]
            print timing_format.format(*timing)
