import os
import random
import time
import sys
import urllib2


def alg1(*args):
    
    pass

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
        for test_set in test_sets.split('\n\n\n\n'):
            lines = map(lambda x: x.strip(), test_set.split('\n'))
            num_lockers, num_keys, num_balls = map(int, lines[1].split(' '))
            given_keys = map(int, lines[2].split(' '))
            desired_lockers = map(int, lines[3].split(' '))
            ans = int(lines[5])
            print str(num_lockers) + ' ' + str(num_keys) + ' ' + str(num_balls)
            print given_keys
            print desired_lockers
            print ans
            print
            print

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
