#!/bin/python
# Source: https://www.hackerrank.com/challenges/absolute-permutation

# We define P to be a permutation of the first N natural numbers in the range [1, N].
# Let p_i denote the position of i in permutation P (please use 1-based indexing).
#
# P is considered to be an absolute permutation if abs(i - p_i) = K holds true for every i in [1, N].
# Given N and K, print the lexicographically smallest absolute permutation, P; if no
# absolute permutation exists, print -1.


def folded_index(i, segment_size):
    a = int(i - 0.1) // segment_size
    if a % 2 == 0:
        return i + segment_size
    else:
        return i - segment_size


def absolute_permutation(size, distance):
    if distance == 0:
        return ' '.join([str(x) for x in xrange(1, size + 1)])
    elif size % 2 == 1:
        return '-1'
    elif size % distance != 0:
        return '-1'
    elif (size / distance) % 2 == 1:
        return '-1'

    result = ''
    for i in xrange(1, size + 1):
        result += ' {}'.format(folded_index(i, distance))

    return result.strip()


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    print absolute_permutation(n, k)