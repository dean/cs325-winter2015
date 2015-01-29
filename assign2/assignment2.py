import os
import random
import time
import sys
import urllib2


DEBUG = False



def count_paths(keys, all_balls, given_balls):
    path = 0
    path = len(keys) + left_path(keys[0], all_balls) + right_path(keys[-1], all_balls)
    if len(keys) == 1:
        return path

    for x in xrange(len(keys) - 1):
        path += total_midpath(keys[x], keys[x+1], all_balls)

    return path

def total_midpath(left_key, right_key, all_balls):
    left_ind = left_key
    biggest_gap = 0
    indices = None
    for x in xrange(left_key, right_key + 1):
        if all_balls[x]:
            gap = x - left_ind
            if gap > biggest_gap:
                biggest_gap = gap
                indices = (left_ind, x)
            left_ind = x

    # Didn't find a ball!
    if not indices:
        return 0

    return right_key - left_key - biggest_gap

def left_path(start, all_balls):
    leftmost = start
    for x in xrange(start - 1, -1, -1):
        if all_balls[x]:
            leftmost = x
    return start - leftmost

def right_path(start, all_balls):
    rightmost = start
    for x in xrange(start + 1, len(all_balls)):
        if all_balls[x]:
            rightmost = x
    return rightmost - start


def powerset(_set):
    if not _set:
        return [[]]
    return (powerset(_set[1:]) +
            [[_set[0]] + x for x in powerset(_set[1:])])


def alg1(num_lockers, num_keys, num_balls, given_keys, desired_lockers):
    if not DEBUG:
        key_sets = powerset(given_keys)
    else:
        from itertools import combinations
        key_sets = combinations(given_keys)
    desired_lockers.sort()
    all_lockers = [x in desired_lockers for x in xrange(num_lockers + 1)]
    total_opened = []
    for keys in key_sets:
        keys.sort()
        if not keys:
            continue
        p = count_paths(keys, all_lockers, desired_lockers)
        total_opened.append(p)
    return min(total_opened)


def alg2(num_keys, num_lockers, num_balls, given_keys, desired_lockers):
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
        arg = None
        if len(sys.argv) > 2:
            arg = sys.argv[2]
            if int(arg) < 1 or int(arg) > 3:
                print 'Algorithm ' + arg + ' does not exist!'
                sys.exit(1)
            if not os.path.exists('test_data' + sys.argv[2] + '.txt'):
                test_data = urllib2.urlopen('http://www.eecs.orst.edu/~glencora/cs325/dp_set' + arg + '.txt')
                with open('test_data' + arg + '.txt', 'w') as f:
                    f.write(test_data.read().replace('\r', ''))
            test_sets = open('test_data' + arg + '.txt', 'r').read().strip()
            chunks = map(lambda x: '\n'.join(x.split('\n')[1:]), test_sets.split('\n\n'))
        else:
            if not os.path.exists('test_data.txt'):
                test_data = urllib2.urlopen('http://www.eecs.orst.edu/~glencora/cs325/dp.txt')
                with open('test_data.txt', 'w') as f:
                    f.write(test_data.read().replace('\r', ''))
            test_sets = open('test_data.txt', 'r').read().strip()
            chunks = map(lambda x: '\n'.join(x.split('\n')[1:4] + [x.split('\n')[5]]), test_sets.split('\n\n\n\n'))

        print len(chunks)
        for i, test_set in enumerate(chunks):
            lines = map(lambda x: x.strip(), test_set.split('\n'))
            num_lockers, num_keys, num_balls = map(int, lines[0].split(' '))
            given_keys = map(int, lines[1].split(' '))
            desired_lockers = map(int, lines[2].split(' '))
            if not arg:
                ans = int(lines[3])
            our_ans = alg1(num_lockers, num_keys, num_balls, given_keys, desired_lockers)
            print 'our ans: ' + str(our_ans)
            if not arg:
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
