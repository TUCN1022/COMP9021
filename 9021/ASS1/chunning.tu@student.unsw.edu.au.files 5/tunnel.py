# -*- encoding:utf-8 -*-
def if_form_correct(data):
    #删除的格式包括：总行数大于2，每一行的数量需要大于2，每一行只能有整数，每行的数量要对应，顶一定要大于底
    for i in range(len(data)):#切割空格
        data[i]=data[i].split()

    for i in range(len(data)):
        for item in data[i]:
            if not item.isdigit():  # isdigit顺便过滤掉非整数
                print('Sorry, input file does not store valid data.')
                exit(0)
    for i in range(len(data)):#全部转为整数
        for j in range(len(data[i])):
            data[i][j]=int(data[i][j])

    #删除：总行数大于2，每一行的数量需要大于2，每行的数量要对应
    if len(data)!=2 or len(data[0])!=len(data[1]) or len(data[0])<2 or len(data[1])<2:
        print('Sorry, input file does not store valid data.')
        exit(0)

    #删除：顶要大于底
    floor_higher_than_ceil = [0] * len(data[0])
    for i in range(len(floor_higher_than_ceil)):
        if data[0][i]<=data[1][i]:
            floor_higher_than_ceil[i]=1
    if sum(floor_higher_than_ceil)!=0:
        print('Sorry, input file does not store valid data.')
        exit(0)
    return data


def dealwith_floor(data):
    # print('在对floor做处理')
    length=len(data[0])#先得到出list长度
    floor,ceiling=data[0],data[1]
    dict_floor={}
    for item in data[0]:#创建floor字典(先获取有的元素），每个元素为键，值为len(n)的0列表。
        dict_floor[item]=[0]*length

    #建立一个ceiling对floor的映射表，放对ceiling中会被影响的点的位置
    ceiling_influence_floor={}
    for floor_item in floor:
        ceiling_influence_floor[floor_item]=[]
        for i in range(len(ceiling)):
            if ceiling[i]>floor_item:
                dict_floor[floor_item][i]=1#直接修改上一步中创建的字典的值，使能被影响的点变为1

    for i in range(length):  # 对列表循环
        for key, value in dict_floor.items():  # 逐个键循环，改变value为需要的list
            if floor[i] <= key:
                value[i] = 1

    all_list=[]
    for key,item in dict_floor.items():
        part_list=[]
        len_value=len(item)
        part_of_length = 0
        for i in range(len_value-1):
            if item[i]==0 and item[i+1]==0:
                part_of_length+=1
            elif item[i]==0 and item[i+1]!=0:
                part_list.append(part_of_length+1)
                part_of_length=0
        if item[-1]==0:

            part_list.append(part_of_length+1)
        all_list.extend(part_list)
    #     print('part_list of {}:'.format(key),part_list,dict_floor[key])
    # print(max(all_list))
    return max(all_list)

# 先得到list长度，然后创建字典(先获取有的元素），每个元素为键，值为len(n)的0列表。
# 以处理ceiling为例：开始循环，按位置顺序遍历。遍历到某个值时，比较各个键和该值的大小，如果值大于等于该键，则该键的值的相应位置改为1
def dealwith_ceiling(data):
    # print('在对ceiling做处理')
    length=len(data[0])#先得到出局长度
    floor,ceiling=data[0],data[1]
    dict_ceiling={}
    for item in data[1]:#创建ceiling字典(先获取有的元素），每个元素为键，值为len(n)的0列表。
        dict_ceiling[item]=[0]*length

    #建立一个ceiling对floor的映射表，放对ceiling中会被影响的点的位置
    floor_influence_ceiling={}
    for ceiling_item in ceiling:
        floor_influence_ceiling[ceiling_item]=[]
        for i in range(len(floor)):
            if floor[i]<ceiling_item:
                dict_ceiling[ceiling_item][i]=1#直接修改上一步中创建的字典的值，使能被影响的点变为1

    for i in range(length):  # 对列表循环
        for key, value in dict_ceiling.items():  # 逐个键循环，改变value为需要的list
            if ceiling[i] >= key:
                value[i] = 1

    all_list=[]
    for key,item in dict_ceiling.items():
        part_list=[]
        len_value=len(item)
        part_of_length = 0
        for i in range(len_value-1):
            if item[i]==0 and item[i+1]==0:
                part_of_length+=1
            elif item[i]==0 and item[i+1]!=0:
                part_list.append(part_of_length+1)
                part_of_length=0
        if item[-1]==0:

            part_list.append(part_of_length+1)
        all_list.extend(part_list)
    #     print('part_list of {}:'.format(key),part_list,dict_ceiling[key])
    # print(max(all_list))
    return max(all_list)


def find_first_tunnel(data):
    floor,ceiling=data[0],data[1]
    a=ceiling[0]
    for i in range(len(floor)):
        if floor[i] <=a:
            return i

if __name__=='__main__':
    filename=input('Please enter the name of the file you want to get data from: ')
    data=[]
    with open(filename,'r',encoding='utf8') as file:
        data_original=file.readlines()
    for item in data_original:
        if not item.isspace():
            data.append(item)
    data=if_form_correct(data)
    if data!=None:
        distance_from_west=find_first_tunnel(data)
        print('From the west, one can into the tunnel over a distance of {}'.format(distance_from_west))
        max_ceiling=dealwith_ceiling(data)
        max_floor=dealwith_floor(data)
        max_distance=max(max_ceiling,max_floor)
        print('Inside the tunnel, one can into the tunnel over a maximum distance of {}'.format(max_distance))

















