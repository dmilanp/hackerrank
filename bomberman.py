#!/bin/python
# Source: https://www.hackerrank.com/challenges/bomber-man

# Initially, Bomberman arbitrarily plants bombs in some of the cells.
# 1 After one second, Bomberman does nothing.
# 2 After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid
# with bombs. It is guaranteed that no bombs will detonate at this second.
# 3 After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands
# back and observes.
# Bomberman then repeats the last two steps indefinitely.
#
# Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs,
# determine the state of the grid after  seconds.


def neighbors(i, j, width, height):
    # type: (int, int, int, int) -> list[tuple(int)]
    _neighbors = [(i, j+1), (i, j-1), (i-1, j), (i+1, j)]
    return [
        x for x in _neighbors
        if (0 <= x[0] < width and
            0 <= x[1] < height)
    ]


def do_plant_bombs(row_count, cols_count, bombs_map):
    bombs_map[3] = {
        (i, j): 1
        for i in xrange(row_count)
        for j in xrange(cols_count)
        if bombs_map[0].get((i, j)) != 1
    }
    return bombs_map


def print_grid(bombs_in, row_count, cols_count):
    output = []
    for i in xrange(row_count):
        line = ''
        for j in xrange(cols_count):
            if (bombs_in[0].get((i, j)) == 1 or
                    bombs_in[1].get((i, j)) == 1 or
                    bombs_in[2].get((i, j)) == 1 or
                    bombs_in[3].get((i, j)) == 1):
                line += 'O'
            else:
                line += '.'
        output.append(line)
    return output


def grid_at_time(grid, N):
    row_count, cols_count = len(grid), len(grid[0])
    bombs_in = {0: {}, 1: {}, 2: {}, 3: {}}

    # Initial bombs
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 'O':
                bombs_in[3][(i, j)] = 1

    output = print_grid(bombs_in, row_count, cols_count)

    if N > 1:
        plants_bombs = False
        side_a, side_b, output = None, None, None
        sufficient_iterations = min(N, 7)

        for t in xrange(1, sufficient_iterations+1):
            bombs_in[0], bombs_in[1], bombs_in[2], bombs_in[3] = bombs_in[1], bombs_in[2], bombs_in[3], {}

            if t == 1:
                plants_bombs = not plants_bombs
                continue

            if plants_bombs:
                bombs_in = do_plant_bombs(row_count, cols_count, bombs_in)

            bomb_locations = list()
            for coordinate, bomb in bombs_in[0].iteritems():
                if bomb == 1:
                    bomb_locations.append(coordinate)

            for bomb_coordinate in bomb_locations:
                bombs_in[0][bomb_coordinate] = 0
                bombs_in[1][bomb_coordinate] = 0
                bombs_in[2][bomb_coordinate] = 0
                for neighbor in neighbors(bomb_coordinate[0], bomb_coordinate[1], row_count, cols_count):
                    bombs_in[0][neighbor] = 0
                    bombs_in[1][neighbor] = 0
                    bombs_in[2][neighbor] = 0

            plants_bombs = not plants_bombs
            output = print_grid(bombs_in, row_count, cols_count)

            if t == 3:
                side_a = output
            elif t == 5:
                side_b = output

    if N <= 7:
        result = output
    else:
        if (N - 8) % 4 in [0, 2]:
            bombs_in = do_plant_bombs(row_count, cols_count, bombs_in)
            output = print_grid(bombs_in, row_count, cols_count)
            result = output
        elif (N - 8) % 4 == 1:
            result = side_b
        elif (N - 8) % 4 == 3:
            result = side_a

    print '\n'.join(result)


rows, cols, N = raw_input().strip().split(' ')
rows, cols, N = int(rows), int(cols), int(N)
grid = []
for __ in xrange(rows):
    row = raw_input().strip()
    grid.append(row)

grid_at_time(grid, N)
