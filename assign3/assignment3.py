def closest_to_zero(O):
    if len(L) == 0:
        return None
    half = len(O)/2
    L, R = O[:half], O[half:]
    ans = min(closest_to_zero(L),
              closest_to_zero(R),
              method3_suffix_prefix(L, R),
              key=lambda x: x[1])

    return min(map(abs, div_and_conquer(L, R)))


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

print method3_suffix_prefix(L, R)
