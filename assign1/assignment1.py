import random
import time
import urllib2
import sys


def enum(arr):
    _max = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            _sum = sum(arr[i:j+1])
            if _sum > _max:
                _max = _sum
    return _max

def better_enum(arr):
    _max = 0
    for i in range(len(arr)):
        _sum = 0
        for j in range(i, len(arr)):
            _sum += arr[j]
            if _sum > _max:
                _max = _sum
    return _max

def dynamic(arr):
    _max = 0
    local_max = 0
    for i in range(len(arr)):
        tmp = local_max + arr[i]
        if tmp < 0:
            local_max = 0
        else:
            local_max = tmp
        if local_max > _max:
            _max = local_max
    return _max

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
            enum_ans = enum(arr)
            print 'enum: Got %d expected %d' % (enum_ans, ans)
            assert(enum(arr) == ans)
            better_enum_ans = better_enum(arr)
            print 'better_enum: Got %d expected %d' % (better_enum_ans, ans)
            assert(better_enum(arr) == ans)
            dynamic_ans = dynamic(arr)
            print 'dynamic: Got %d expected %d\n' % (dynamic_ans, ans)
            assert(dynamic(arr) == ans)

    elif sys.argv[1] == '--time':
        random.seed(931915823)
        print 'Size |   Alg 1   |   Alg 2  |   Alg 3   '
        timing_format = '{:<5} {:^11} {:^11} {:^11}'
        for size in xrange(100, 1001, 100):
            timings = [[], [], []]
            for i in range(10):
                arr = [random.randint(-100, 100) for x in xrange(size)]
                for j, alg in enumerate([enum, better_enum, dynamic]):
                    start = time.clock()
                    alg(arr)
                    timings[j].append(round(time.clock() - start, 11))
            timing = [size] + map(lambda x: sum(x)/float(len(x)), timings)
            print timing_format.format(*timing)

        #  dynamic Only.
        for size in xrange(2000, 9001, 1000):
            timings = []
            for i in range(10):
                arr = [random.randint(0, 100) for x in xrange(size)]
                start = time.clock()
                dynamic(arr)
                timings.append(time.clock() - start)
            t = round(sum(timings)/float(len(timings)), 11)
            timing = [size, '', '', t]
            print timing_format.format(*timing)
