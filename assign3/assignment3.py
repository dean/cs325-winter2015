


def div_and_conquer(L, R):
    return min(map(abs, div_and_conquer(L, R)))

def method1_suffix_prefix(L, R):
    l_best, r_best = len(L) - 1, 0
    for i in xrange(len(L) - 1, -1, -1):
        for j in xrange(len(R)):
            if abs(L[i] + R[j]) < abs(L[l_best] + R[r_best]):
                l_best, r_best = i, j

    return L[l_best] + R[r_best]

def method2_suffix_prefix(L, R):
    L.sort()
    R.sort()

def method3_suffix_prefix(L, R):
    new_l = [(e, True, i) for i, e in enumerate(L)]
    inversed = [(e * -1, False, i) for i, e in enumerate(R)]
    new_l += inversed
    new_l = sorted(new_l, key=lambda x: x[0])

    smallest_gap = None
    for i in xrange(len(new_l) - 1):
        cur, _next = new_l[i], new_l[i + 1]
        if cur[1] == _next[1]:
            continue

        gap_width = abs(cur[0] - _next[0])
        if (not smallest_gap or
                (gap_width < abs(smallest_gap[0][0] - smallest_gap[1][0]))):
             smallest_gap = (cur, _next)

    return smallest_gap

# def method3(l, r):
#     new_l = [(e, True, i) for i, e in enumerate(L)]
#     inversed = [(e * -1, False, i) for i, e in enumerate(R)]
#     new_l += inversed
#     new_l = sorted(new_l, key=lambda x: x[0])
# 
#     for i, item in enumerate(new_l):
#         if i < len(new_l):
#             current, _next = item, new_l[i+1]
#             if current[1] == _next[1]:
#                 continue
#             diff = abs(current[0] - _next[0]



L = [22, -9, 32, -27, -53]
R = [58, 52, 149, 56, 33]

print method3_suffix_prefix(L, R)
