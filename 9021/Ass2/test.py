# -*- encoding:utf-8 -*-
import numpy as np
class FriezeError(Exception):
    def __init__(self, ErrorInfo):
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return self.ErrorInfo

if __name__ == '__main__':
    height_correct = True
    length_correct = True
    every_two_line_same = True
    for i in range(1, 5):
        file_name = '/Users/simontu/Desktop/UNSW/9021/Ass2/home/incorrect_input_' + str(i) + '.txt'
        print(file_name)
        with open(file_name) as file:
            file_data = []
            data = file.readlines()
            for line in data:
                if not line.isspace():
                    # 读取grid数据
                    line_data = []
                    for digit_str in line.split():
                        line_data.append(int(digit_str))
                    file_data.append(line_data)
        # file_data
        # 判断文件读取是否符合条件
        # the_file_data=np.array(file_data)
        # print(np.shape(the_file_data))
        line_len = len(file_data[0])
        for item in file_data:
            len_of_line = len(item)
            if len_of_line != line_len:
                every_two_line_same = False
                break
        for item in file_data:
            len_of_line = len(item)
            if len_of_line > 50 or len_of_line < 4:
                length_correct = False
                break
        if len(file_data) < 2 or len(file_data) > 16:
            height_correct = False
        if not length_correct or not height_correct or not every_two_line_same:

            raise FriezeError('frieze.FriezeError: Incorrect input.')
        else:
            pass