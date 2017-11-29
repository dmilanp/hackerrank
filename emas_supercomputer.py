#!/bin/python
# Source: https://www.hackerrank.com/challenges/two-pluses

# Given a grid of size M x N, each cell in the grid is either good or bad.
# A valid plus is defined here as the crossing of two segments (horizontal
# and vertical) of equal lengths. These lengths must be odd, and the middle
# cell of its horizontal segment must cross the middle cell of its vertical segment.

# Find 2 pluses that can be drawn on good cells of the grid, and print
# an integer denoting the maximum product of their areas.
#
#


def neighbors(i, j, width, height):
    # type: (int, int, int, int) -> iterator[tuple(int)]
    _neighbors = [(i, j+1), (i, j-1), (i-1, j), (i+1, j)]
    return (
        x for x in _neighbors
        if (0 <= x[0] < width and
            0 <= x[1] < height)
    )


def edges_of_plus_of_size(center, size):
    # type: (tuple, int) -> list
    i, j = center
    return [
        (i - size, j),
        (i + size, j),
        (i, j - size),
        (i, j + size),
    ]


def split_initial_grid_to_dictionaries(grid, rows, cols):
    # type: (dict, int, int) -> tuple
    good, bad, grid_dict = {}, {}, {}
    for i in xrange(rows):
        for j in xrange(cols):
            if grid[i][j] == 'G':
                good[(i, j)] = 'G'
                grid_dict[(i, j)] = 'G'
            else:
                bad[(i, j)] = 'B'
                grid_dict[(i, j)] = 'B'
    return good, bad, grid_dict


def expandable_plus_at_coordinates(good_dict, distance, grid_dict):
    # type: (dict, int, dict) -> dict
    new_good_dict = {}

    for coordinate in good_dict.iterkeys():
        should_add = True
        center = (coordinate[0], coordinate[1],)
        for distant_neighbor in edges_of_plus_of_size(center=center, size=distance):
            if distant_neighbor not in grid_dict or grid_dict[distant_neighbor] == 'B':
                should_add = False
        if should_add:
            new_good_dict[coordinate] = 'G'

    return new_good_dict


def elements_in_plus_at_center_with_size(center, size):
    # type: (tuple, int) -> set
    plus_set = set([center])
    for r in xrange(size):
        plus_set.update(
            edges_of_plus_of_size(center=center, size=r+1)
        )
    return plus_set


def find_highest_feasible_partner(top_candidate, sorted_options):
    """
    :param top_candidate: (value, center, elements_contained)
    :param sorted_options: list[(value, center, elements_contained)]
    :return:
    """
    for option in sorted_options:
        if not set(top_candidate[2]).intersection(set(option[2])):
            return option
    return None


def plus_pair_score(top_reference, highest_partner):
    """
    :param top_reference: (value, center, elements_contained)
    :param highest_partner: (value, center, elements_contained)
    :return:
    """
    if top_reference and highest_partner:
        return top_reference[0] * highest_partner[0]
    return 0


def biggest_plus_per_coordinate(good_dict, bad_dict, grid_dict):
    pluses_by_value = {}

    assert len(good_dict) >= 2

    value = 1
    pluses_by_value[value] = {
        coordinate: [coordinate]
        for coordinate
        in good_dict.iterkeys()
    }

    # Neighbors of bad cells can't grow

    for bad_coordinate in bad_dict.iterkeys():
        for neighbor in neighbors(bad_coordinate[0], bad_coordinate[1], rows, cols):
            try:
                good_dict.pop(neighbor)
            except KeyError:
                pass

    reach = 1
    good_dict = expandable_plus_at_coordinates(good_dict, reach, grid_dict)

    while len(good_dict):
        value += 4
        pluses_by_value[value] = {}

        for coordinate in good_dict.iterkeys():
            pluses_by_value[value][coordinate] = elements_in_plus_at_center_with_size(center=coordinate, size=reach)

        reach += 1
        good_dict = expandable_plus_at_coordinates(good_dict, reach, grid_dict)

    return pluses_by_value


def maximum_area(grid, rows, cols):
    # type: (dict, int, int) -> None

    # Build dict of largest plus per coordinate

    good_dict, bad_dict, grid_dict = split_initial_grid_to_dictionaries(grid, rows, cols)
    pluses_by_value = biggest_plus_per_coordinate(good_dict, bad_dict, grid_dict)

    # Put pluses by coordinate in a sorted list by plus dimension

    sorted_options = []

    for plus_size, plus_coordinates in sorted(pluses_by_value.iteritems(), reverse=True):
        for center, coordinates in list(plus_coordinates.iteritems()):
            sorted_options.append((plus_size, center, coordinates))

    positive_sorted_options = [x for x in sorted_options if x[0] > 1]

    _max = 1

    options_count = len(positive_sorted_options)
    for i, candidate in enumerate(positive_sorted_options):

        highest_partner = find_highest_feasible_partner(candidate, positive_sorted_options[min(i + 1, options_count - 1):])
        if highest_partner:
            s = plus_pair_score(candidate, highest_partner)
            if s > _max:
                _max = s
        else:
            if candidate[0] > _max:
                _max = candidate[0]

    print _max


rows, cols = raw_input().strip().split(' ')
rows, cols = int(rows), int(cols)
grid = []
for __ in xrange(rows):
    row = raw_input().strip()
    grid.append(row)

maximum_area(grid, rows, cols)
