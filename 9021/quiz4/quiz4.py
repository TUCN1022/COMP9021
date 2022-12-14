import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
      )
print()

directions = {0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1),
              4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1)
              }

p = (0,0)
lit_points = {p:1}
code = int(code)
min_x = max_x=0
min_y = max_y = 0

do=True
while code or do:
    do=False
    temp=code%8
    code=code//8
    new_p_list=[0,0]
    for i in range(2):
        new_p_list[i]=p[i]+directions[temp][i]
    new_p=tuple(new_p_list)
    if new_p not in lit_points:
        lit_points[new_p]=1
    else:
        lit_points[new_p]*=-1
    p=new_p

for i in range(nb_of_leading_zeroes):
    for i in range(2):
        new_p_list[i] = p[i] + directions[0][i]
    new_p = tuple(new_p_list)
    if new_p not in lit_points:
        lit_points[new_p] = 1
    else:
        lit_points[new_p] *= -1
    p = new_p

delete_key=[]
for key,value in lit_points.items():
    if value==-1:
        delete_key.append(key)
for key in delete_key:
    del lit_points[key]

if lit_points:
    for key, value in lit_points.items():
        min_x = min(min_x, key[0])
        max_x = max(max_x, key[0])
        min_y = min(min_y, key[1])
        max_y = max(max_y, key[1])
    x_len=max_x-min_x+1
    y_len=max_y-min_y+1
    # a=[[off]*x_len]*y_len
    a=[]
    for i in range(y_len):
        a.append([off]*x_len)


    for key,value in lit_points.items():

        if value==1:
            the_i=max_y-key[1]
            the_j=-min_x+key[0]
            a[the_i][the_j]=on



    for i in range(y_len):
        result = ''
        for j in range(x_len):
            result+=a[i][j]
        print(result)
        # print()
