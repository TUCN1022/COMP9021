# -*- encoding:utf-8 -*-
import csv
from pathlib import Path

path = Path('names')
targeted_first_name = input('Enter a male first name: ')
year_dict={}#用来放放满足的年份
rank_list=[]
for year in range(1880,2021):
    subfile_name='yob'+str(year)+'.txt'
    file_name=path/subfile_name
    if not file_name.exists():
        continue
    with open(file_name,'r',encoding='utf8') as file:
        all_data=file.readlines()
        all_amount=0
        amount_name=0
        rank=1
        rank_dict={}
        one_year_dict={}#用来存放该年的男人名和人数
        for item in all_data:
            name,gender,amount=item.split(',')
            if name==targeted_first_name:
                amount_name=int(amount)
            if gender=='M':
                all_amount+=int(amount)
                one_year_dict[name]=int(amount)
                if int(amount) in rank_dict:
                    rank_dict[int(amount)] += 1
                else:
                    rank_dict[int(amount)] = 1
        rank_dict_sort = sorted(rank_dict.items(), reverse=True)
        for item in rank_dict_sort:
            key,value=item[0],item[1]
            if key!=amount_name:
                rank+=value
            else:
                rank_list.append(rank)
                break
        for key,value in one_year_dict.items():
            if key==targeted_first_name:
                year_dict[year]=[rank,value/all_amount]
                break


if not year_dict:
    print(targeted_first_name,'is not a male first name in my records.')
else:
    # print('year_dict:',year_dict)
    # print('rank_list:',rank_list)

    min_rank=min(rank_list)
    # print('min_rank:', min_rank)
    # print(sorted(rank_list))
    min_year_dict={}
    for key,value in year_dict.items():
        if value[0]==min_rank:
            min_year_dict[key]=value
    min_year_sort=sorted(min_year_dict.items(), key=lambda x:x[1][1], reverse=True)
    print('By decreasing order of frequency,',targeted_first_name ,'was most popular in the following years:')
    for i in range(len(min_year_sort)):
        if i%5==0:
            print('   ',min_year_sort[i][0],end='')
        elif i%5==4:
            print('',min_year_sort[i][0])
        else:
            print('',min_year_sort[i][0],end='')
    if i%5==4:
        print('Its rank was', min_rank, 'then.')
    else:
        print('\nIts rank was', min_rank, 'then.')







#Matthew
