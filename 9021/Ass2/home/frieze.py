# -*- encoding:utf-8 -*-
import numpy as np


# np.set_printoptions(threshold=np.inf)
class FriezeError(Exception):
    def __init__(self, ErrorInfo):
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return self.ErrorInfo


class Frieze():
    def __init__(self, file_name):
        self.file_name = file_name
        self.height_correct = True
        self.length_correct = True
        self.every_two_line_same = True

        self.frieze_first1 = True
        self.frieze_first2 = True
        self.frieze_last1 = True
        self.frieze_last2 = True

        # 打开文件
        with open(self.file_name) as file:
            file_data = []
            data = file.readlines()
            for line in data:
                if not line.isspace():
                    # 读取grid数据
                    line_data = []
                    for digit_str in line.split():
                        line_data.append(int(digit_str))
                    file_data.append(line_data)

        # 判断文件读取是否符合生成条件
        line_len = len(file_data[0])
        for item in file_data:
            len_of_line = len(item)
            if len_of_line != line_len:
                self.every_two_line_same = False
                break
        for item in file_data:
            len_of_line = len(item)
            if len_of_line > 51 or len_of_line < 5:
                self.length_correct = False
                break
        if len(file_data) < 3 or len(file_data) > 17:
            self.height_correct = False

        # 判断文件读取是否符合frieze条件
        first_line = file_data[0]
        last_line = file_data[-1]
        for i in range(len(first_line) - 1):
            if first_line[i] not in (4, 12):
                self.frieze_first1 = False
                break
        for i in range(len(last_line) - 1):
            if last_line[i] not in (4, 5, 6, 7):
                self.frieze_last1 = False

                break
        if first_line[-1] != 0:
            self.frieze_first2 = False
        if last_line[-1] != 0:
            self.frieze_last2 = False

        if not self.length_correct or not self.height_correct or not self.every_two_line_same:
            raise FriezeError('Incorrect input.')
            exit()
        elif not self.frieze_first1 or not self.frieze_first2 or not self.frieze_last1 or not self.frieze_last2:
            print(self.frieze_first1, self.frieze_first2, self.frieze_last1, self.frieze_last2)
            raise FriezeError('Input does not represent a frieze.')
            exit()

        # 转换成numpy
        self.file_data = np.array(file_data, dtype='int')
        self.file_data_jgg_grid = np.array(self.generate_jgg_grid())

    # 生成九宫格
    def generate_jgg_grid(self):
        height = len(self.file_data)
        width = len(self.file_data[0])
        jgg_grid = np.zeros((height * 3, width * 3), dtype='int')
        # 生成初始九宫格
        for row in range(height):
            for col in range(width):
                num = self.file_data[row][col]
                # 把num转换为二进制
                num_base2 = f"{num:04b}"
                points = []
                if num_base2[-1] == '1':
                    jgg_grid[row * 3][col * 3 + 1] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1

                if num_base2[-2] == '1':
                    jgg_grid[row * 3][col * 3 + 2] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1

                if num_base2[-3] == '1':
                    jgg_grid[row * 3 + 1][col * 3 + 2] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1

                if num_base2[-4] == '1':
                    jgg_grid[row * 3 + 2][col * 3 + 2] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1

        # 判断周围九宫格的影响
        for row in range(height):
            for col in range(width):
                # 左边的影响
                if col * 3 + 1 - 2 > 0 and jgg_grid[row * 3 + 1][col * 3 + 1 - 2] == 1:
                    jgg_grid[row * 3 + 1][col * 3] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1
                # 左上的影响
                if col * 3 + 1 - 2 > 0 and row * 3 + 1 - 2 > 0 and jgg_grid[row * 3 + 1 - 2][col * 3 + 1 - 2] == 1:
                    jgg_grid[row * 3][col * 3] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1
                # 左下的影响
                if col * 3 + 1 - 2 > 0 and row * 3 + 1 + 2 < height * 3 and jgg_grid[row * 3 + 1 + 2][
                    col * 3 + 1 - 2] == 1:
                    jgg_grid[row * 3 + 1 + 1][col * 3] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1
                # 下的影响
                if row * 3 + 1 + 2 < height * 3 and jgg_grid[row * 3 + 1 + 2][col * 3 + 1] == 1:
                    jgg_grid[row * 3 + 1 + 1][col * 3 + 1] = 1
                    jgg_grid[row * 3 + 1][col * 3 + 1] = 1
        return jgg_grid

    # 竖线坐标输出
    def print_out1(self):
        array1 = self.file_data_jgg_grid
        result = []
        for col in range(1, len(array1[0]), 3):
            row = 0
            while row < len(array1):
                length = 0
                if array1[row][col] == 1:
                    the_row = row
                    while array1[row][col] == 1:
                        row += 1
                        length += 1
                    if length > 1:
                        # print(length)
                        result.append([(col // 3, the_row // 3), (col // 3, (the_row // 3) + (length // 3))])
                else:
                    row += 1
        return result

    # 西北到东南坐标输出
    def print_out2(self):
        array2 = self.file_data_jgg_grid
        result = []
        for row in range(1, len(array2), 3):  # 从原始的第一行开始逐渐遍历
            for col in range(1, len(array2[0]), 3):  # 从原始的第一列开始横向遍历
                row1 = row
                col1 = col
                while row1 < len(array2) and col1 < len(array2[0]):
                    length = 0
                    if array2[row1][col1] == 1:
                        the_row = row1
                        the_col = col1
                        while array2[row1][col1] == 1 and row1 < len(array2) and col1 < len(array2[0]):
                            row1 += 1
                            col1 += 1
                            length += 1
                        if length > 1:
                            need_to_add = True
                            for item in result:
                                if (col1 // 3, (the_row // 3) + (length // 3)) == item[1]:
                                    need_to_add = False
                                    break
                            if need_to_add:
                                result.append(
                                    [(the_col // 3, the_row // 3), (col1 // 3, (the_row // 3) + (length // 3))])
                    else:
                        row1 += 1
                        col1 += 1
        result = sorted(result, key=lambda x: (x[0][1], x[0][0]))
        return result

    # 横线坐标输出
    def print_out3(self):
        array3 = self.file_data_jgg_grid
        result = []
        for row in range(1, len(array3), 3):
            col = 0
            while col < len(array3[0]):
                length = 0
                if array3[row][col] == 1:
                    the_col = col
                    while array3[row][col] == 1:
                        col += 1
                        length += 1
                    if length > 1:
                        result.append([(the_col // 3, row // 3), ((the_col // 3) + (length // 3), row // 3)])
                else:
                    col += 1
        return result

        # 假设文件已经读出来了要开始判断
        # self.generate_nine_grid()
        # self.check_period()
        # self.check_reflection()

    # 西南到东北坐标输出
    def print_out4(self):
        array4 = self.file_data_jgg_grid
        result = []
        for row in range(1, len(array4), 3):  # 从原始的第一行开始逐渐遍历
            for col in range(1, len(array4[0]), 3):  # 从原始的第一列开始横向遍历
                row1 = row
                col1 = col
                while row1 >= 0 and col1 < len(array4[0]):
                    length = 0
                    if array4[row1][col1] == 1:
                        the_row = row1
                        the_col = col1
                        while array4[row1][col1] == 1 and row1 >= 0 and col1 < len(array4[0]):
                            row1 -= 1
                            col1 += 1
                            length += 1
                        if length > 1:
                            need_to_delete = []
                            for item in result:
                                if (col1 // 3, (the_row // 3) - (length // 3)) == item[1]:
                                    need_to_delete.append(item)
                            for item in need_to_delete:
                                result.remove(item)
                            result.append([(the_col // 3, the_row // 3), (col1 // 3, (the_row // 3) - (length // 3))])
                    else:
                        row1 -= 1
                        col1 += 1
        result = sorted(result, key=lambda x: x[0][1])
        return result

        # 假设文件已经读出来了要开始判断
        # self.generate_nine_grid()
        # self.check_period()
        # self.check_reflection()

    def analyse(self):
        have_perod = False
        horizontal = False
        vertical = False
        glided_horizontal = False
        glided_vertical = False
        rotation = False
        number_dict = {0: {},
                       1: {1: 1},
                       2: {2: 1},
                       3: {1: 1, 2: 1},
                       4: {4:1},
                       5: {4: 1, 1: 1},
                       6: {4: 1, 2: 1},
                       7: {4: 1, 2: 1, 1: 1},
                       8: {8: 1},
                       9: {8: 1, 1: 1},
                       10: {8: 1, 2: 1},
                       11: {8: 1, 2: 1, 1: 1},
                       12: {8: 1, 4: 1},
                       13: {8: 1, 4: 1, 1: 1},
                       14: {8: 1, 4: 1, 2: 1},
                       15: {8: 1, 4: 1, 2: 1, 1: 1},
                       }

        period = 0
        grid = self.file_data.copy()
        jgg_grid = self.generate_jgg_grid()
        for i in range(1, len(grid[0]) // 2 + 1):
            can_get = True
            for j in range(1, len(grid[0]) // i):
                if not (grid[:, :i] == grid[:, i * j:i * (j + 1)]).all():
                    can_get = False
                    break
            if can_get == True:
                period = i
                have_perod = True
                break

        the_jgg_grid = jgg_grid
        for i in range(period * 3):
            the_jgg_grid = np.roll(the_jgg_grid, 1, axis=1)
            if (the_jgg_grid[:, :period * 3] == np.flipud(the_jgg_grid[:, :period * 3])).all():
                horizontal = True
            if (the_jgg_grid[:, :period * 3] == np.rot90(the_jgg_grid[:, :period * 3], 2)).all():
                rotation = True
#########################################################################################################################
        number_grid = []
        number_grid_line=[]
        for i in range(len(grid[0])):
            number_grid_line.append({})
        for i in range(len(grid)):
            number_grid.append(number_grid_line)

        number_grid = np.array(number_grid)
        for i in range(len(number_grid)):
            for j in range(len(number_grid[0])):
                number_grid[i, j] = number_dict[grid[i,j]].copy()  # 生成number字典的grid
        # # print(np.shape(number_grid))
        if period % 2 == 1:
            the_number_grid = number_grid[:,:-1].copy()
            the_number_grid2 = number_grid[:, :-1].copy()
            for i in range(period):  # 转动次数，次数最多为period
                the_number_grid = np.roll(the_number_grid2, i, axis=1)
                goto = False
                for j in range(len(the_number_grid)):  # 某次比较中比较的行数
                    for k in range(period // 2):  # 某次比较中比较的列数
                        if 1 in the_number_grid[j, k].keys():  # 比较1和对称位置
                            if 1 in the_number_grid[j, period - k].keys():
                                del the_number_grid[j, k][1]
                                del the_number_grid[j, period - k][1]
                            else:
                                goto = True
                                break
                        if 2 in the_number_grid[j, k].keys():  # 比较2和对称位置
                            if 8 in the_number_grid[j - 1, period - k - 1].keys():
                                del the_number_grid[j, k][2]
                                del the_number_grid[j - 1, period - k - 1][8]
                            else:
                                goto = True
                                break
                        if 4 in the_number_grid[j, k].keys():  # 比较4和对称位置
                            if 4 in the_number_grid[j, period - k - 1].keys():
                                # print(period)
                                # print(i,j,k,the_number_grid[j, k])
                                # print(i,j,period - k - 1,the_number_grid[j, period - k - 1])
                                del the_number_grid[j, k][4]
                                del the_number_grid[j, period - k - 1][4]
                            else:
                                goto = True
                                break
                        if 8 in the_number_grid[j, k].keys():  # 比较8和对称位置
                            if 2 in the_number_grid[j + 1, period - k - 1].keys():
                                del the_number_grid[j, k][8]
                                del the_number_grid[j+1, period - k - 1][2]
                            else:
                                goto = True
                                break
                    if goto == True:
                        break
                    k = period // 2
                    for l in range(len(the_number_grid)):  # 把中间列也处理了
                        if 1 in the_number_grid[l, k].keys():  # 比较1和对称位置
                            if 1 in the_number_grid[l, k + 1].keys():
                                del the_number_grid[l, k][1]
                                del the_number_grid[l, k + 1][1]
                        if 4 in the_number_grid[l, k].keys():  # 比较4和对称位置
                            del the_number_grid[l, k][4]
            count_number = 0
            for i in range(len(the_number_grid)):  # 某次比较中比较的行数
                for j in range(period):  # 某次比较中比较的列数
                    if not the_number_grid[i, j]:
                        count_number += 1
            if count_number == len(the_number_grid) * period:
                vertical = True

###############################################################################################
        else:
            period += 1  # 加一列再比较
            the_number_grid2 = number_grid.copy()[:,:-1]
            # the_number_grid2 = the_number_grid.copy()

            for i in range(period):  # 转动次数，次数最多为period
                the_number_grid = np.roll(the_number_grid2, i, axis=1).copy()
                print(the_number_grid2[:, :period], '\n')
                goto = False
                for j in range(len(the_number_grid)):  # 某次比较中比较的行数
                    print('结点1：', the_number_grid2[:, :period])
                    for k in range(period // 2):  # 某次比较中比较的列数
                        if 1 in the_number_grid[j, k]:  # 比较1和对称位置
                            if 1 in the_number_grid[j, period - k]:
                                del the_number_grid[j, k][1]
                                del the_number_grid[j, period - k][1]
                            else:
                                goto = True
                                break
                        if 2 in the_number_grid[j, k]:  # 比较2和对称位置
                            if 8 in the_number_grid[j - 1, period - k - 1]:
                                del the_number_grid[j, k][2]
                                del the_number_grid[j - 1, period - k - 1][8]
                            else:
                                goto = True
                                break
                        if 4 in the_number_grid[j, k]:  # 比较4和对称位置
                            if 4 in the_number_grid[j, period - k - 1]:
                                del the_number_grid[j, k][4]
                                del the_number_grid[j, period - k - 1][4]
                            else:
                                goto = True
                                break
                        if 8 in the_number_grid[j, k]:  # 比较8和对称位置
                            if 2 in the_number_grid[j + 1, period - k - 1]:
                                del the_number_grid[j, k][8]
                                del the_number_grid[j+1, period - k - 1][2]
                            else:
                                goto = True
                                break
                    if goto == True:
                        break

                    k = period // 2
                    for l in range(len(the_number_grid)):  # 把中间行也处理了
                        if 1 in the_number_grid[l, k]:  # 比较1和对称位置
                            if 1 in the_number_grid[l, k + 1]:
                                del the_number_grid[l, k][1]
                                del the_number_grid[l, k + 1][1]
                        if 4 in the_number_grid[l, k]:  # 比较4和对称位置
                            del the_number_grid[l, k][4]

                count_number = 0
                for i in range(len(the_number_grid)):  # 某次比较中比较的行数
                    for j in range(period):  # 某次比较中比较的列数
                        if not the_number_grid[i, j]:
                            count_number += 1
                if count_number == len(the_number_grid) * period:
                    vertical = True
            period-=1


        # print(self.)
        if have_perod == True and vertical == False and horizontal == False and rotation == False and glided_horizontal == False and glided_vertical == False:
            print('Pattern is a frieze of period ', period, ' that is invariant under translation only.', sep='')
        elif have_perod == True and vertical == True and horizontal == False and rotation == False and glided_horizontal == False and glided_vertical == False:
            print('Pattern is a frieze of period ', period,
                  ' that is invariant under translation\n', '        and vertical reflection only.', sep='')
        elif have_perod == True and vertical == False and horizontal == True and rotation == False and glided_horizontal == False and glided_vertical == False:
            print('Pattern is a frieze of period ', period,
                  ' that is invariant under translation\n', '        and horizontal reflection only.', sep='')
        elif have_perod == True and vertical == False and horizontal == False and rotation == False and glided_horizontal == True and glided_vertical == False:
            print('Pattern is a frieze of period ', period,
                  ' that is invariant under translation\n', '        and glided horizontal reflection only.', sep='')
        elif have_perod == True and vertical == False and horizontal == False and rotation == True and glided_horizontal == False and glided_vertical == False:
            print('Pattern is a frieze of period ', period,
                  ' that is invariant under translation\n', '        and rotation only.',
                  sep='')
        elif have_perod == True and vertical == False and horizontal == False and rotation == True and glided_horizontal == True and glided_vertical == True:
            print('Pattern is a frieze of period ', period,
                  ' that is invariant under translation\n',
                  '        glided horizontal and vertical reflections, and rotation only.',
                  sep='')
        elif have_perod == True and vertical == True and horizontal == True and rotation == True and glided_horizontal == False and glided_vertical == False:
            print('Pattern is a frieze of period ', period,
                  ' that is invariant under translation,\n',
                  '        horizontal and vertical reflections, and rotation only.',
                  sep='')

    def display(self):
        # generate_name = '/'.join(self.file_name.split('/')[:-1]) + '/' + self.file_name.split('/')[-1][:-4] + '.tex'
        generate_name = str(self.file_name)[:-4] + '.tex'
        with open(generate_name, 'w+') as tex_file:
            tex_file.write('\\documentclass[10pt]{article}\n')
            tex_file.write('\\usepackage{tikz}\n')
            tex_file.write('\\usepackage[margin=0cm]{geometry}\n')
            tex_file.write('\\pagestyle{empty}\n\n')
            tex_file.write('\\begin{document}\n\n')
            tex_file.write('\\vspace*{\\fill}\n')
            tex_file.write('\\begin{center}\n')
            tex_file.write('\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n')

            tex_file.write('% North to South lines\n')
            for item in self.print_out1():
                content = '    \draw (' + str(item[0][0]) + ',' + str(item[0][1]) + ') -- (' + str(
                    item[1][0]) + ',' + str(item[1][1]) + ');\n'
                tex_file.write(content)
            tex_file.write('% North-West to South-East lines\n')
            for item in self.print_out2():
                content = '    \draw (' + str(item[0][0]) + ',' + str(item[0][1]) + ') -- (' + str(
                    item[1][0]) + ',' + str(item[1][1]) + ');\n'
                tex_file.write(content)
            tex_file.write('% West to East lines\n')
            for item in self.print_out3():
                content = '    \draw (' + str(item[0][0]) + ',' + str(item[0][1]) + ') -- (' + str(
                    item[1][0]) + ',' + str(item[1][1]) + ');\n'
                tex_file.write(content)
            tex_file.write('% South-West to North-East lines\n')
            for item in self.print_out4():
                content = '    \draw (' + str(item[0][0]) + ',' + str(item[0][1]) + ') -- (' + str(
                    item[1][0]) + ',' + str(item[1][1]) + ');\n'
                tex_file.write(content)

            tex_file.write('\\end{tikzpicture}\n')
            tex_file.write('\\end{center}\n')
            tex_file.write('\\vspace*{\\fill}\n\n')
            tex_file.write('\\end{document}\n')
        tex_file.close()


if __name__ == '__main__':
    # for i in range(1, 8):
    #     some_filename = '/Users/simontu/Desktop/UNSW/9021/Ass2/home/frieze_' + str(i) + '.txt'
    #     print(some_filename)
        some_filename = '/Users/simontu/Desktop/UNSW/9021/Ass2/home/frieze_2.txt'
        frieze = Frieze(some_filename)
        if frieze:
            frieze.analyse()
            frieze.display()
