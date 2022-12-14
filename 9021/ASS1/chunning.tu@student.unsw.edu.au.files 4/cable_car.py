# -*- encoding:utf-8 -*-
import os

def if_form_correct(data):
    # 删除的格式包括：只能是正整数，严格单调递增,至少两个
    for i in range(len(data)):  # 切割空格
        data[i] = data[i].split()
    deal_data = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            deal_data.append(data[i][j])

    for item in deal_data:
        if not item.isdigit() or item == '0':  # 过滤掉非正整数
            print('Sorry, input file does not store valid data.')
            exit(0)
    if len(deal_data) < 2:
        print('Sorry, input file does not store valid data.')
        exit(0)
    for i in range(len(deal_data)):
        deal_data[i]=int(deal_data[i])
    if_sis = []  # 是否严格单调递增正整数
    for i in range(1, len(deal_data)):
        if_sis.append(deal_data[i] - deal_data[i - 1])
    for item in if_sis:
        if item <= 0:
            print('Sorry, input file does not store valid data.')
            exit(0)
    return deal_data


def whether_perfect(data):
    gap = data[1] - data[0]
    stop = 0
    for i in range(1, len(data)):
        if (data[i] - data[i - 1]) != gap:
            print('The ride could be better...')
            stop = 1
            break
    if stop == 0:
        print('The ride is perfect!')


def longest_perfect_length(data_list):
    data = data_list.copy()
    minus_list = []
    for i in range(1, len(data)):
        minus_list.append(data[i] - data[i - 1])
    result = [1] * len(minus_list)
    for i in range(1, len(minus_list)):
        if minus_list[i] == minus_list[i - 1]:
            result[i] = result[i] + result[i - 1]
    return max(result)


def remove_number(data_list):
    data=data_list.copy()
    length=len(data)
    result_dict={}
    for i in range(1,length):
        for j in range(i):
            difference=data[i]-data[j]
            if (data[j],data[j]-difference) not in result_dict:
                result_dict[(data[i],data[j])]=2
            else:
                result_dict[(data[i],data[j])]=result_dict[(data[j],data[j]-difference)]+1
    result_sort=sorted(result_dict.items(),key=lambda x:x[1],reverse=True)
    return length-result_sort[0][1]






if __name__ == '__main__':
    filename = input('Please enter the name of the file you want to get data from: ')
    data = []
    if not os.path.exists(filename):
        print('Sorry, there is no such file.')
    else:
        with open(filename, 'r', encoding='utf8') as file:
            data_original = file.readlines()

        for item in data_original:
            if not item.isspace():
                data.append(item)

        data = if_form_correct(data)
        if data:
            whether_perfect(data)
            lpl = longest_perfect_length(data)
            print('The longest good ride has a length of: {}'.format(lpl))
            delete_number = remove_number(data)
            print('The minimal number of pillars to remove to build a perfect ride from the rest is: {}'.format(
                delete_number))

#cable_car_1.txt
