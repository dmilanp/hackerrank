#!/bin/python
# Source: https://www.hackerrank.com/challenges/encryption

# Sample Input:
# haveaniceday
#
# Sample Output:
# hae and via ecy

from math import ceil, floor, sqrt

s = raw_input().strip()
without_spaces = ''.join(s.split(' '))
length = len(without_spaces)
rows = int(floor(sqrt(length)))
cols = int(ceil(sqrt(length)))

containers = [[] for __ in xrange(cols)]
for i, letter in enumerate(without_spaces):
    containers[i % cols].append(letter)

print(' '.join(
    ''.join(container)
    for container in containers
))