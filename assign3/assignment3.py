import os
import random
import time
import sys
import urllib2


def closest_to_zero(O, method):
    if len(O) < 2:
        return (abs(O[0][0]), O[0][1], O[0][1])
    half = len(O)/2
    L, R = O[:half], O[half:]
    suffices = sum_of_suffices(L)
    prefices = sum_of_prefices(R)
    left = closest_to_zero(L, method)
    right = closest_to_zero(R, method)
    both = method(suffices, prefices)
    ans = min(left, right, both, key=lambda x: x[0])

    return ans

def sum_of_suffices(L):
    cur = [L[-1]]
    for x in L[:-1][::-1]:
        cur.append((cur[-1][0] + x[0], x[1]))
    return cur[::-1]

def sum_of_prefices(R):
    cur = [R[0]]
    for x in R[1:]:
        cur.append((cur[-1][0] + x[0], x[1]))
    return cur

def method3_suffix_prefix(L, R):
    new_l = [(e[0], True, e[1]) for e in L]
    inversed = [(e[0] * -1, False, e[1]) for e in R]
    new_l += inversed
    new_l = sorted(new_l, key=lambda x: x[0])

    smallest_gap = None
    for i in xrange(len(new_l) - 1):
        cur, _next = new_l[i], new_l[i + 1]
        if cur[1] == _next[1]:
            continue

        gap_width = abs(cur[0] - _next[0])
        if (not smallest_gap or
                gap_width < abs(smallest_gap[0][0] - smallest_gap[1][0])):
            smallest_gap = (cur, _next, gap_width)

    if smallest_gap[1][1]:
        smallest_gap = (smallest_gap[1], smallest_gap[0], smallest_gap[2])

    return (smallest_gap[2], smallest_gap[0][2], smallest_gap[1][2])


# Correct iput for closest to zero
# L = [31, -41, 59, 26, -53]
# R = [58, -6, 97, -93, -23]
# O = L + R
# i, j, s = closest_to_zero(O, method3_suffix_prefix)
# 
# assert abs(sum(O[i:j + 1])) == s
# 
# 
# L = [22, -9, 32, -27, -53]
# R = [58, 52, 149, 56, 33]
# O = L+R
# print closest_to_zero(O, method3_suffix_prefix)
# print method3_suffix_prefix(L, R)




if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print 'Usage: python assignment1.py [option]'
        print 'Options:'
        options = ['--test', '--time <# runs>']
        print '\n'.join(map(lambda x:'\t'+ x, options))
        sys.exit()

    elif sys.argv[1] == '--test':
        test_set_url = 'http://web.engr.oregonstate.edu/~glencora/cs325/ctz/test_cases_with_solutions.txt'
        chunks = urllib2.urlopen(test_set_url).read().strip().replace('\r', '').split('\n')

        for test_set in chunks:
            inp, s, ind1, ind2 = eval(test_set)

            correct = (s, ind1, ind2)
            ans = closest_to_zero(zip(inp, xrange(len(inp))), method3_suffix_prefix)

            print correct
            print ans

            assert(correct == ans)


    elif sys.argv[1] == '--solve':
        test_set_url = 'https://eecs.orst.edu/~glencora/cs325/ctz/test_cases_without_solutions.txt'
        chunks = urllib2.urlopen(test_set_url).read().strip().replace('\r', '').split('\n')
        for test_set in chunks:
            inp = eval(test_set)
            s, ind1, ind2 = closest_to_zero(zip(inp, xrange(len(inp))), method3_suffix_prefix)
            print s, ind1, ind2



