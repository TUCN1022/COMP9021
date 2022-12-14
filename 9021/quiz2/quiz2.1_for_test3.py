# -*- encoding:utf-8 -*-
# -*- encoding:utf-8 -*-
# Written by *** for COMP9021
#
# Besides a function to generate a random dictionary,
# defines two functions that analyse a dictionary.
# See the pdf for explanations via an illustration
# and examples of possible uses.
#
# You can assume that both functions are called with proper
# arguments (namely, a dictionary whose keys are all integers
# between 1 and n for some strictly positive integer n
# and whose values are numbers between 1 and n,
# and an integer between 1 and n).
#
# The lines that are output by the
# function longest_strictly_decreasing_sequences_to()
# are ordered from smallest first value to largest first value.


from random import seed, randint

def generate_mapping(for_seed, length):
    seed(for_seed)
    return {i: randint(1, length) for i in range(1, length + 1)}

def follow_the_arrows_from(mapping, n):
    # 首先key和 value先存起来，通过不断删除起始点找到loop的值
    # loop的值通过一个循环开始 找到到自己结束 （以此区分出有几个loop）
    keys_list=[]#所有的key
    values_list=[]#所有的value
    loop=[]#环
    find_loop=mapping.copy()
    for key, value in mapping.items():#把key和value存起来
        keys_list.append(key)
        values_list.append(value)

    while sorted(list(find_loop.keys()))!=sorted(list(find_loop.values())):#通过不断对比key和value找出环的值
        #先建立key和value的列表
        temp_keys_list = []
        temp_values_list = []
        for key, value in find_loop.items():  # 把key和value存起来
            temp_keys_list.append(key)
            temp_values_list.append(value)
        # print('到这一步了1',sorted(temp_keys_list),sorted(temp_values_list))

        #找只有出度没有入度的值（头），删除头
        for i in range(1,len(mapping)+1):
            # print('到这一步了2',i)
            if i not in temp_values_list and i in temp_keys_list:#条件1：没有入度；条件2：有出度
                # print('有要删的')
                del find_loop[i]

    # print('2:找出loop了',find_loop)
    while find_loop:#找出有几个环
        temp_loop=[]
        key_into_loop=list(find_loop.keys())[0]
        while key_into_loop not in temp_loop:
            temp_loop.append(key_into_loop)
            a=find_loop[key_into_loop]#先把这个key存起来，如果直接赋值下一步删除的就是新的key
            del find_loop[key_into_loop]
            key_into_loop = a
        loop.append(temp_loop)

    loop_dist={}
    for item in loop:
        for i in item:
            loop_dist[i] = len(item)
    #输出结果
    if n in loop_dist:
        print('It is on a loop of length',loop_dist[n])
    else:
        distance=0
        key = n
        while True:
            if key not in loop_dist.keys():
                key=mapping[key]
                distance+=1
            else:
                print('It starts with a stalk of length', distance)
                print('It reaches', key, 'on a loop of length', loop_dist[key])
                break


def longest_strictly_decreasing_sequences_to(mapping, n):
    if n not in mapping.values():
        return
    result_list=[]
    queue=[[n]]
    while len(queue)>0:
        temp=queue.pop(0)
        switch=False
        for key, value in mapping.items():
            if value==temp[0] and key>value:
                switch = True
                a=temp.copy()
                a.insert(0,key)
                queue.append(a)

        del mapping[temp[0]]
        if switch==False:
            result_list.append(temp)

    print(result_list)
    max_len_of_result=max([len(i) for i in result_list])
    for item in result_list:
        if len(item)==max_len_of_result:
            result = ''
            for i in range(max_len_of_result-1):
                result+=str(item[i])
                result+=' -> '
            result+=str(item[-1])
            print(result)





mapping = generate_mapping(61, 11)
print(mapping)
#{1: 8, 2: 3, 3: 9, 4: 4, 5: 6, 6: 5, 7: 6, 8: 1, 9: 8, 10: 6, 11: 6}
follow_the_arrows_from(mapping, 6)
print()
#It is on a loop of length 2
follow_the_arrows_from(mapping, 4)
print()
#It is on a loop of length 1
longest_strictly_decreasing_sequences_to(mapping, 5)
print()
#7 -> 6 -> 5
# 10 -> 6 -> 5
# 11 -> 6 -> 5
