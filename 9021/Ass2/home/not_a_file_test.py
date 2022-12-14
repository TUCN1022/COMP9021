# -*- encoding:utf-8 -*-
import numpy as np

# #########################################################################################################################
# else:
# the_number_grid = number_grid.copy()
# for i in range(period):  # 转动次数，次数最多为period
#     the_number_grid = np.roll(the_number_grid, 1, axis=1)
#     goto = False
#     for j in range(len(the_number_grid)):  # 某次比较中比较的行数
#         the_number_grid = number_grid
#         for k in range(period // 2):  # 某次比较中比较的列数
#             if 1 in the_number_grid[j, k]:  # 比较1和对称位置
#                 if 1 in the_number_grid[j, period - k]:
#                     del the_number_grid[j, k][1]
#                     del the_number_grid[j, period - k][1]
#                 else:
#                     goto = True
#                     break
#             if 2 in the_number_grid[j, k]:  # 比较2和对称位置
#                 if 2 in the_number_grid[j - 1, period - k - 1]:
#                     del the_number_grid[j, k][2]
#                     del the_number_grid[j - 1, period - k - 1][8]
#                 else:
#                     goto = True
#                     break
#             if 4 in the_number_grid[j, k]:  # 比较4和对称位置
#                 if 4 in the_number_grid[j, period - k - 1]:
#                     del the_number_grid[j, k][4]
#                     # del the_number_grid[j, period - k - 1][4]
#                 else:
#                     goto = True
#                     break
#             if 8 in the_number_grid[j, k]:  # 比较8和对称位置
#                 if 2 in the_number_grid[j + 1, period - k - 1]:
#                     del the_number_grid[j, k][8]
#                     del the_number_grid[j, period - k - 1][2]
#                 else:
#                     goto = True
#                     break
#         if goto == True:
#             break
#         k = period // 2
#         for l in range(len(the_number_grid)):  # 把中间行也处理了
#             # if 1 in the_number_grid[l][k]:  # 比较1和对称位置
#             #     if 1 in the_number_grid[l][k+1]:
#             #         del the_number_grid[l][k][1]
#             #         del the_number_grid[l][k+1][1]
#             if 4 in the_number_grid[l, k]:  # 比较4和对称位置
#                 del the_number_grid[l, k][4]
# count_number = 0
# for i in range(len(the_number_grid)):  # 某次比较中比较的行数
#     for j in range(period):  # 某次比较中比较的列数
#         if not the_number_grid[i, j]:
#             count_number += 1
# if count_number == len(the_number_grid) * period:
#     vertical = True
#
# period += 1  # 加一列再比较
# the_number_grid = number_grid.copy()
# for i in range(period):  # 转动次数，次数最多为period
#     the_number_grid = np.roll(the_number_grid, 1, axis=1)
#     goto = False
#     for j in range(len(the_number_grid)):  # 某次比较中比较的行数
#         the_number_grid = number_grid
#         for k in range(period // 2):  # 某次比较中比较的列数
#             if 1 in the_number_grid[j, k]:  # 比较1和对称位置
#                 if 1 in the_number_grid[j, period - k]:
#                     del the_number_grid[j, k][1]
#                     del the_number_grid[j, period - k][1]
#                 else:
#                     goto = True
#                     break
#             if 2 in the_number_grid[j, k]:  # 比较2和对称位置
#                 if 2 in the_number_grid[j - 1, period - k - 1]:
#                     del the_number_grid[j, k][2]
#                     del the_number_grid[j - 1, period - k - 1][8]
#                 else:
#                     goto = True
#                     break
#             if 4 in the_number_grid[j, k]:  # 比较4和对称位置
#                 if 4 in the_number_grid[j, period - k - 1]:
#                     del the_number_grid[j, k][4]
#                     del the_number_grid[j, period - k - 1][4]
#                 else:
#                     goto = True
#                     break
#             if 8 in the_number_grid[j, k]:  # 比较8和对称位置
#                 if 2 in the_number_grid[j + 1, period - k - 1]:
#                     del the_number_grid[j, k][8]
#                     del the_number_grid[j, period - k - 1][2]
#                 else:
#                     goto = True
#                     break
#         if goto == True:
#             break
#         k = period // 2
#         for l in range(len(the_number_grid)):  # 把中间行也处理了
#             if 1 in the_number_grid[l, k]:  # 比较1和对称位置
#                 if 1 in the_number_grid[l, k + 1]:
#                     del the_number_grid[l, k][1]
#                     del the_number_grid[l, k + 1][1]
#             if 4 in the_number_grid[l, k]:  # 比较4和对称位置
#                 del the_number_grid[l, k][4]
# count_number = 0
# for i in range(len(the_number_grid)):  # 某次比较中比较的行数
#     for j in range(period):  # 某次比较中比较的列数
#         if not the_number_grid[i, j]:
#             count_number += 1
# if count_number == len(the_number_grid) * period:
#     vertical = True

number_dict={1:{1:1},
                2:{2:1},
                3:{1:1,2:1},
                4: {4: 1},
                5: {4: 1,1:1},
                6: {4: 1,2:1},
                7: {4: 1,2:1,1:1},
                8: {8: 1},
                9: {8: 1,1:1},
                10: {8: 1,2:1},
                11: {8: 1, 2: 1, 2: 1},
                12: {8: 1, 4: 1},
                13: {8: 1, 4: 1,1:1},
                14: {8: 1,4: 1,2:1},
                15: {8: 1, 4: 1, 2: 1, 1: 1},
                }

del number_dict[5][1]
del number_dict[5][4]
# del number_dict[5][45]
print(number_dict[5])

a=[{},{}]
if a==[{}]*3:
    print(1)

if 1 in number_dict[1]:
    del number_dict[1][1]
    print(number_dict[1])
print(number_dict[15].keys())


a=np.array([[1,2,3],[4,5,6]])
b=np.roll(a,1,axis=1)
print(b)