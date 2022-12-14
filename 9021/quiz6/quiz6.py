# Written by *** and Eric Martin for COMP9021
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
# 第一题57 58 68 69

from random import seed, randrange
import sys

dim = 10


def display_grid(grid):
    for row in grid:
        print('   ', *row)


def size_of_largest_parallelogram(grid, dim):
    max_size = 0
    for i in range(dim):  # 从某一行开始往下找
        for j in range(dim):  # 遍历某一行的长度
            for k in range(2, dim):  # 遍历时的长度
                row = 0
                if j + k <= dim and grid[i][j:j + k] == [1] * k:
                    row += 1
                    for l in range(i + 1, dim):#和下面的行做比较
                        if grid[l][j:j + k] == [1] * k:
                            row += 1
                        else:
                            break
                    # print(1,row, k)
                if row > 1:
                    max_size = max(max_size, row * k)

                row = 0
                if j + k <= dim and grid[i][j:j + k] == [1] * k:
                    row += 1
                    for l in range(i + 1, dim):
                        l2=1

                        if j - l2 >= 0 and grid[l][j - l2:j - l2 + k] == [1] * k:
                            row += 1
                            l2+=1

                        else:
                            break

                if row > 1:
                    max_size = max(max_size, row * k)
                    # print('满足的行数row：', row, '满足的列数k:', k, '从第几行开始：', i, '从第几列开始:', j)

                row = 0
                if j + k <= dim and grid[i][j:j + k] == [1] * k:
                    row += 1
                    for l in range(i + 1, dim):
                        if j + row + k < dim and grid[l][j + row:j + row + k] == [1] * k:
                            row += 1

                        else:
                            break
                    # print(3,row, k)
                if row > 1:
                    max_size = max(max_size, row * k)

    return max_size
    # REPLACE PASS ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS


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
display_grid(grid)
size = size_of_largest_parallelogram(grid,dim)
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')
