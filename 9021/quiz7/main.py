# Written by *** for COMP9021

# Prompts the user for a seed, a dimension dim, and an upper bound N.
# Randomly fills a grid of size dim x dim with numbers between 0 and N
# and computes:
# - the largest value n such that there is a path of the form (0, 1, 2,... N);
# - the number of such paths.
# A path is obtained by repeatedly moving in the grid one step North, South,
# West or East.


import sys
from random import seed, randint


def display_grid():
    for row in grid:
        print(' '.join(f'{e:{len(str(upper_bound))}}' for e in row))

def value_and_number_of_longest_paths(grid):
    path_len = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            length=0
            stack_data=[]
            if grid[i][j]==0:
                stack_data.append(((i,j),length))
                while stack_data:
                    add_new=0
                    point=stack_data.pop(-1)
                    if point[0][0]-1>=0 and grid[point[0][0]-1][point[0][1]]==grid[point[0][0]][point[0][1]]+1:#上
                        length=grid[point[0][0]-1][point[0][1]]
                        stack_data.append(((point[0][0]-1,point[0][1]),length))
                        add_new=1
                    if point[0][0]+1<len(grid) and grid[point[0][0]+1][point[0][1]]==grid[point[0][0]][point[0][1]]+1:#下
                        length=grid[point[0][0]+1][point[0][1]]
                        stack_data.append(((point[0][0]+1,point[0][1]),length))
                        add_new = 1
                    if point[0][1]-1>=0 and grid[point[0][0]][point[0][1]-1]==grid[point[0][0]][point[0][1]]+1:#左
                        length=grid[point[0][0]][point[0][1]-1]
                        stack_data.append(((point[0][0],point[0][1]-1),length))
                        add_new = 1
                    if point[0][1]+1<len(grid[0]) and grid[point[0][0]][point[0][1]+1]==grid[point[0][0]][point[0][1]]+1:#右
                        length=grid[point[0][0]][point[0][1]+1]
                        stack_data.append(((point[0][0],point[0][1]+1),length))
                        add_new = 1
                    if add_new==0:
                        path_len.append(point[1])
    max_path=max(path_len)
    how_many=0
    for i in range(len(path_len)):
        if path_len[i]==max_path:
            how_many+=1





    return max_path,how_many
    # REPLACE THE RETURN STATEMENT WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS

provided_input = input('Enter three integers: ').split()
if len(provided_input) != 3:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    for_seed, dim, upper_bound = (abs(int(e)) for e in provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, upper_bound) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

max_value, nb_of_paths_of_max_value = value_and_number_of_longest_paths(grid)
if not nb_of_paths_of_max_value:
    print('There is no 0 in the grid.')
else:
    print('The longest paths made up of consecutive numbers starting '
          f'from 0 go up to {max_value}.'
         )
    if nb_of_paths_of_max_value == 1:
        print('There is one such path.')
    else:
        print('There are', nb_of_paths_of_max_value, 'such paths.')