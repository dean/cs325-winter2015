import random
import time
import urllib2
import sys


def alg1(arr):
    _max = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            _sum = sum(arr[i:j+1])
            if _sum > _max:
                _max = _sum
    return _max

def alg2(arr):
    _max = 0
    for i in range(len(arr)):
        _sum = 0
        for j in range(i, len(arr)):
            _sum += arr[j]
            if _sum > _max:
                _max = _sum
    return _max

def alg3(arr):
    pass

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Usage: python assignment1.py [option]'
        print 'Options:'
        options = ['--test', '--time']
        print '\n'.join(map(lambda x:'\t'+ x, options))
        sys.exit()

    elif sys.argv[1] == '--test':
        test_sets = open('test_data.txt', 'r').read().strip()
        for test_set in test_sets.split('\n\n'):
            inp = map(int, test_set.replace(',', '').replace('[', '').replace(']', '').strip().split(' '))
            arr, ans = inp[:-1], inp[-1]
            print 'Input: {0}'.format(arr)
            alg1_ans = alg1(arr)
            print 'Alg1: Got %d expected %d' % (alg1_ans, ans)
            # assert(alg1(arr) == ans)
            alg2_ans = alg2(arr)
            print 'Alg2: Got %d expected %d' % (alg2_ans, ans)
            assert(alg2(arr) == ans)
            # Test here

    elif sys.argv[1] == '--time':
        random.seed(931915823)
        print 'Size |   Alg 1   |   Alg2   |   Alg3   '
        timing_format = '{:<5} {:^11} {:^11} {:^11}'
        for size in xrange(100, 1001, 100):
            arr = [random.randint(0, 100) for x in xrange(size)]
            timing = []
            for alg in [alg1, alg2]:
                start = time.clock()
                alg(arr)
                timing.append(time.clock() - start)
            timing = [size] + timing + ['']
            print timing_format.format(*timing)

        '''
        #  Alg3 Only.
        for size in xrange(2000, 9001, 1000):
            arr = [random.randint(0, 100) for x in xrange(size)]
            lines = sorted(map(lambda x: Line(*x), zip(ms, bs)), key=lambda x: x.m)
            timing = []
            start = time.clock()
            alg(lines)
            timing.append(time.clock() - start)
            timing = [size, '', ''] + timing + [0]
            print timing_format.format(*timing)
        '''
