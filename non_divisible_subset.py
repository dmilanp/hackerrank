#!/bin/python
# Source: https://www.hackerrank.com/challenges/non-divisible-subset

# Given a set, S, of n distinct integers, print the size of a maximal subset
# S', of S where the sum of any 2 numbers in S' is not evenly divisible by k.

from collections import defaultdict

def max_non_divisible_subset(n, k, a):
    remainder_sets = defaultdict(list)
    count = 0

    for element in a:
        remainder_sets[element % k].append(element)

    for j in xrange(k // 2 + 1):
        if j == 0 or (j == k // 2 and k % 2 == 0):
            count += min(1, len(remainder_sets[j]))
        else:
            count += max(
                len(remainder_sets[j]),
                len(remainder_sets[k - j]),
            )

    return count


n, k = [int(num) for num in raw_input().strip().split(' ')]
a = [int(num) for num in raw_input().strip().split(' ')]
result = max_non_divisible_subset(n, k, a)
print result
