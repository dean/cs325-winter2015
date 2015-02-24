def closest_to_zero(O, method):
    if len(L) == 0:
        return None
    half = len(O)/2
    L, R = O[:half], O[half:]
    suffices = sum_of_suffices(L)
    prefices = sum_of_prefices(R)
    ans = min(filter(lambda x: x, closest_to_zero(suffices)),
              filter(lambda x: x, closest_to_zero(prefices)),
              method(L, R),
              key=lambda x: x[1])

    return ans

def sum_of_suffices(L):
    cur = [L[-1]]
    for x in L[:-1][::-1]:
        cur.append(cur[-1] + x)
    return cur[::-1]

def sum_of_prefices(R):
    cur = [R[0]]
    for x in R[1:]:
        cur.append(cur[-1] + x)
    return cur

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
        smaller_gap = gap_width < abs(smallest_gap[0][0] - smallest_gap[1][0])
        if not smallest_gap or smaller_gap:
             smallest_gap = (cur, _next)

    return smallest_gap


L = [22, -9, 32, -27, -53]
R = [58, 52, 149, 56, 33]


L = [31, -41, 59, 26, -53]
print sum_of_suffices(L)
R = [58, -6, 97, -93, -23]
print sum_of_prefices(R)

# O = L+R
# print closest_to_zero(O, method3_suffix_prefix)
# print method3_suffix_prefix(L, R)
