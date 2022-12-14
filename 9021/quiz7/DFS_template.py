
from random import seed, randrange

for_seed=0
sparsity=4
i=2
j=7
seed(for_seed)
grid = [[int(randrange(sparsity) == 0) for _ in range(10)]
            for _ in range(10)
       ]
print('The grid is:')
for row in grid:
    print(*row)


print('The area of the largest empty region of the grid')
print(f'containing the point ({i}, {j}) is: ', end='')
# INSERT YOUR CODE HERE
# max_area=0

area=0
# if grid[i][j]==0:
stack_data=[(i,j)]
grid[i][j]=1
area+=1
while stack_data:
    point=stack_data.pop(-1)
    # print(point[1]+1,len(grid[0]))
    if point[1]<len(grid[0]) and grid[point[0]][point[1]+1]==0:
        stack_data.append((point[0],point[1]+1))
        grid[point[0],point[1]+1]=1
        area+=1
    if point[1]-1>=0 and grid[point[0],point[1]-1]==0:
        stack_data.append((point[0],point[1]-1))
        grid[point[0], point[1] - 1] = 1
        area+=1
    if point[0]+1<len(grid) and grid[point[0]+1,point[1]]==0:
        stack_data.append((point[0]+1,point[1]))
        grid[point[0]+1, point[1] ] = 1
        area+=1
    if point[0]-1>=0 and grid[point[0]-1,point[1]]==0:
        stack_data.append((point[0]-1,point[1]))
        grid[point[0] - 1, point[1]] = 1
        area+=1
max_area=max(max_area,area)
print(area)