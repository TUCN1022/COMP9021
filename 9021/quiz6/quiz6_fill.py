# Written by *** for COMP9021
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram():
    max_size = 0
    for i in range(dim - 1):
        for j1 in range(dim - 1):
            ***
            for j2 in range(j1 + 1, dim):
                ***
                max_size = max(***,
                               largest_with_top_side(i, j1, j2, 'straight'),
                               largest_with_top_side(i, j1, j2, 'left'),
                               largest_with_top_side(i, j1, j2, 'right')
                              )
    return max_size


def largest_with_top_side(i1, j1, j2, direction):
    length = j2 - j1 + 1
    i2 = i1
    if direction == 'straight':
        ***
    elif direction == 'left':
        ***
    else:
        ***
    if i2 == i1 + 1:
        return 0
    return (i2 - i1) * length


try: 
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')