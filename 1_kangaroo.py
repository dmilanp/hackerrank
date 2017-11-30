#!/bin/python
# Source: https://www.hackerrank.com/challenges/kangaroo

# There are two kangaroos on a number line ready to jump in the positive direction
# (i.e, toward positive infinity). The first kangaroo starts at location  and moves at
# a rate of  meters per jump. The second kangaroo starts at location  and moves at a
# rate of  meters per jump. Given the starting locations and movement rates for each kangaroo,
# can you determine if they'll ever land at the same location at the same time?


def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        print "YES"

    gap = x1 - x2
    gap_2 = x1 + v1 - x2 - v2
    gap_diff = abs(gap_2) - abs(gap)

    if gap_diff >= 0:
        return "NO"

    if gap % gap_diff == 0:
        return "YES"

    return "NO"


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
