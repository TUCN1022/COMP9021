
# -*- encoding:utf-8 -*-
'''
3 5 8.5
3 5 8
4 -3 1 2 -7
-7 1 2 3 4
1 2 3 4 5
'''

def deal_error_form(input_str):  # 先判断输入是否符合格式。再判断修改次数是否超过长度
    input_str = input_str.split()
    input_list=[]

    for item in input_str:
        turnto_negative=1
        if item[0]=='-':
            item=item[1:]
            turnto_negative=-1
        if not item.isdigit():  # isdigit顺便过滤掉非整数
            print('Sorry, these are not valid power values.')
            exit(0)
        input_list.append(turnto_negative*int(item))
    return input_list


def first_question(positive,negative,nb_of_switches):
    #随意转换，先区分正负，然后正负都排序，可以的话就把所有负的转为正的，不够的话把优先转
    #换小的负的，超了的话对所有变成正的数做排序，把剩下的次数都给最小那个做操作
    positive_list=positive.copy()
    negative_list=negative.copy()
    num_positive=len(positive_list)
    num_negative=len(negative_list)
    if nb_of_switches<=num_negative:
        for i in range(nb_of_switches):
            negative_list[i]=negative_list[i]*-1
        return sum(positive_list+negative_list)
    else:
        for i in range(num_negative):
            negative_list[i]=negative_list[i]*-1
        rest_of_switches=nb_of_switches-num_negative
        all_list=positive_list+negative_list
        all_list.sort()
        for i in range(rest_of_switches):
            all_list[0]=all_list[0]*-1
        return sum(all_list)


def second_question(positive,negative,nb_of_switches):
    # 随意转换，先区分正负，然后正负都排序，可以的话就把所有负的转为正的，不够的话把优先转
    # 换小的负的，超了的话只能对原本为正的数做排序，把剩下的次数都给最小的那几个数
    positive_list=positive.copy()
    negative_list=negative.copy()
    num_positive = len(positive_list)
    num_negative = len(negative_list)
    if nb_of_switches <= num_negative:
        for i in range(nb_of_switches):
            negative_list[i] = negative_list[i] * -1
        all_list=positive_list+negative_list
        return sum(all_list)
    else:
        for i in range(num_negative):
            negative_list[i] = negative_list[i] *-1
        rest_switches = nb_of_switches - num_negative
        for i in range(rest_switches):
            positive_list[i] = positive_list[i] * -1

        return sum(negative_list+positive_list)


def third_question(input_list,nb_of_switches):
    result=[]
    data=input_list.copy()
    for i in range(len(data)-nb_of_switches+1):
        temp=data[:i]
        for j in range(nb_of_switches):
            temp.append(data[i+j]*-1)
        temp.extend(data[i+nb_of_switches:])
        result.append(sum(temp))
    return max(result)




def fourth_question(input_list):
    deal_list=[0]
    for i in range(len(input_list)):
        if deal_list[i]>=0:
            if input_list[i]>=0:
                deal_list.append(0)
            else:
                deal_list.append(input_list[i])
        else:
            deal_list.append(input_list[i]+deal_list[-1])
    return sum(input_list)-2*min(deal_list)









if __name__ == '__main__':
    input_str = input("Please input the heroes' powers: ")
    if input_str.strip() == '':
        nb_of_switches = int(input("Please input the number of power flips: "))
        if nb_of_switches == 0:
            print(
                'Possibly flipping the power of the same hero many times, the greatest achievable power is 0.')
            print('Flipping the power of the same hero at most once, the greatest achievable power is 0.')
            print(
                'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is 0.')
            print(
                'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is 0.')
    input_list = deal_error_form(input_str)
    if input_list:
        nb_of_switches = int(input("Please input the number of power flips: "))
        if nb_of_switches > len(input_list):
            print('Sorry, this is not a valid number of power flips.')
            exit(0)
        else:
            positive = []
            negative = []
            for item in input_list:
                if item<0:
                    negative.append(item)
                else:
                    positive.append(item)

            positive.sort()
            negative.sort()

            question1_answer = first_question(positive,negative,nb_of_switches)
            question2_answer = second_question(positive,negative,nb_of_switches)
            question3_answer = third_question(input_list,nb_of_switches)
            question4_answer = fourth_question(input_list)

            print('Possibly flipping the power of the same hero many times, the greatest achievable power is {}.'.format(
                question1_answer))
            print('Flipping the power of the same hero at most once, the greatest achievable power is {}.'.format(
                question2_answer))
            print('Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {}.'.format(
                question3_answer))
            print('Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {}.'.format(
                question4_answer))



