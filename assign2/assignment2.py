import os
import random
import time
import sys
import urllib2


def shortest_key_path(keys, locker):
    return min(key - locker if key >= locker else locker - key for key in keys)


def powerset(_set):
    if not _set:
        return [[]]
    return (powerset(_set[1:]) +
            [[_set[0]] + x for x in powerset(_set[1:])])


def alg1(num_keys, num_lockers, num_balls, given_keys, desired_lockers):
    key_sets = powerset(given_keys)
    desired_lockers.sort()
    all_lockers = [False if x not in desired_lockers else True
                   for x in xrange(desired_lockers[-1] + 1)]
    total_opened = []
    for keys in key_sets:
        num_opened = len(keys)
        if not keys:
            continue
        for locker, has_ball in enumerate(all_lockers):
            if has_ball:
                step_count = shortest_key_path(keys, locker)
                if locker not in keys:
                    keys.append(locker)
                num_opened += step_count
        total_opened.append(num_opened)
    return min(total_opened)


def alg2(*args):
    pass


def alg3(*args):
    pass

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Usage: python assignment1.py [option]'
        print 'Options:'
        options = ['--test', '--time <# runs>']
        print '\n'.join(map(lambda x:'\t'+ x, options))
        sys.exit()

    elif sys.argv[1] == '--test':
        if not os.path.exists('test_data.txt'):
            test_data = urllib2.urlopen('http://www.eecs.orst.edu/~glencora/cs325/dp.txt')
            with open('test_data.txt', 'w') as f:
                f.write(test_data.read().replace('\r', ''))

        test_sets = open('test_data.txt', 'r').read().strip()
        for i, test_set in enumerate(test_sets.split('\n\n\n\n')):
            if i != 3:
                continue
            lines = map(lambda x: x.strip(), test_set.split('\n'))
            num_lockers, num_keys, num_balls = map(int, lines[1].split(' '))
            given_keys = map(int, lines[2].split(' '))
            desired_lockers = map(int, lines[3].split(' '))
            ans = int(lines[5])
            our_ans = alg1(num_lockers, num_keys, num_balls, given_keys, desired_lockers)
            print 'our ans: ' + str(our_ans)
            print 'real ans: ' + str(ans)

    elif sys.argv[1] == '--time':
        random.seed(935182318)
        all_timings = [[], [], []]
        print 'Size |   Alg 1   |   Alg 2  |   Alg 3   '
        timing_format = '{:<5} {:^11} {:^11} {:^11}'
        for size in xrange(100, 1000, 100):
            timings = [[], [], []]
            for i in range(int(sys.argv[2])):
                arr = [random.randint(-100, 100) for x in xrange(size)]
                for j, alg in enumerate([alg1, alg2, alg3]):
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
                for j, alg in enumerate([alg2, alg3]):
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
