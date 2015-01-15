import random
import time
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
    _sum = 0
    for i in range(len(arr)):
        tmp = _sum + arr[i]
        if tmp < 0:
            _sum = 0
        else:
            _sum = tmp
        if _sum > _max:
            _max = _sum
    return _max

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Usage: python assignment1.py [option]'
        print 'Options:'
        options = ['--test', '--time <# runs>']
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
        all_timings = [[], [], []]
        print 'Size |   Alg 1   |   Alg 2  |   Alg 3   '
        timing_format = '{:<5} {:^11} {:^11} {:^11}'
        for size in xrange(100, 1000, 100):
            timings = [[], [], []]
            for i in range(int(sys.argv[2])):
                arr = [random.randint(-100, 100) for x in xrange(size)]
                for j, alg in enumerate([enum, better_enum, dynamic]):
                    start = time.clock()
                    alg(arr)
                    timings[j].append(round(time.clock() - start, 11))
            timing = [size] + map(lambda x: sum(x)/float(len(x)), timings)
            print timing_format.format(*timing)
            for i, t in enumerate(timings):
                all_timings[i].append(t)

        #  dynamic Only.
        for size in xrange(1000, 9001, 1000):
            timings =[[], []]
            for i in range(int(sys.argv[2])):
                for j, alg in enumerate([better_enum, dynamic]):
                    arr = [random.randint(0, 100) for x in xrange(size)]
                    start = time.clock()
                    alg(arr)
                    timings[j].append(time.clock() - start)
            t = round(sum(timings[0])/float(len(timings[0])), 11)
            t2 = round(sum(timings[1])/float(len(timings[1])), 11)
            timing = [size, 0, t, t2]
            print timing_format.format(*timing)
            all_timings[0].append(0)
            all_timings[1].append(t)
            all_timings[2].append(t2)
