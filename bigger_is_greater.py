#!/bin/python
# Source: https://www.hackerrank.com/challenges/bigger-is-greater

# Given a word w, rearrange the letters of w to construct another word s in such a way
# that s is lexicographically greater than w. In case of multiple possible answers,
# find the lexicographically smallest one among them.


def next_bigger_word(word):
    word = list(word)
    index_to_swap = -1
    index_to_swap_to_the_left = -1
    for index_to_move_left in xrange(len(word) - 1, -1, -1):

        if index_to_move_left < index_to_swap:
            break

        for index_to_move_right in xrange(index_to_move_left - 1, -1, -1):
            if word[index_to_move_right] < word[index_to_move_left] and index_to_move_right > index_to_swap:
                index_to_swap = index_to_move_right
                index_to_swap_to_the_left = index_to_move_left

    if index_to_swap == -1:
        return "no answer"

    intact_part = ''.join(word[:index_to_swap])
    word[index_to_swap], word[index_to_swap_to_the_left] = word[index_to_swap_to_the_left], word[index_to_swap]
    sorted_rest = ''.join(sorted(word[index_to_swap + 1:]))

    return '{}{}{}'.format(intact_part, word[index_to_swap], sorted_rest)


n = int(raw_input().strip())
input_words = []
for __ in xrange(n):
    input_words.append(raw_input().strip())

for word in input_words:
    print next_bigger_word(word)