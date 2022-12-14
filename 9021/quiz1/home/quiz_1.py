# Written by *** for COMP9021
#
# Prompts the user for two strictly positive integers,
# then used to draw a 'picture'.
#
# Also prompts the user for the name of a file, assumed to be
# stored in the working directory, to then read its contents
# and output derived sentences.
#
# The file can contain anywhere any number of blank lines
# (that is, lines containing an arbitrary number of spaces
# and tabs--an empty line being the limiting case).
#
# Nonblank lines are always of the form:
# person_name, profession:year_of_birth--year_of_death
# with no space anywhere except after the comma and between
# the various parts of person_name; in particular, there is
# no space before person_name and no space after year_of_death.
# year_of_birth and year_of_death are strictly positive integers
# (so DC years), the difference between both being at least 2.


import sys
from os.path import exists

try:
    plus_number, dash_number =\
            (int(x) for x in input('Enter two strictly positive integers '
                                   'for the picture dimensions: '
                                  ).split()
            )
    if plus_number <= 0 or dash_number <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
file_name = input('Input the name of a file in the working directory: ')
if not exists(file_name):
    print('Incorrect input, giving up.')
    sys.exit()

# INSERT YOUR CODE HERE
# def print_boundary(plus_number,dash_number):
#     print('*','+*'*plus_number,dash_number*3,'+*'*plus_number,'*',sep='')



def print_picture(plus_number,dash_number):
    print('*', '+*' * plus_number, '-'* dash_number, '*+' * plus_number, '*', sep='')
    print('*',' '*(plus_number*4+dash_number),'*',sep='')
    print('*',' '*(plus_number*2),'*'*dash_number,' '*(plus_number*2),'*',sep='')
    print('*', ' ' * (plus_number * 4 + dash_number), '*', sep='')
    print('*', '+*' * plus_number,'-'* dash_number, '*+' * plus_number, '*', sep='')

def print_file(file_name):
    with open(file_name,'r',encoding='utf8') as file1:
        data=file1.readlines()
        for item in data:
            if not item.isspace():
                name,others=item.split(',')
                job,years=others.split(':')
                job=job.strip()
                # print(years,years[-4:],years[:4])
                age=int(years[6:])-int(years[:4])
                print('* The',job,'"'+name+'"','lived for',age,'many years.')
print("First, here is some kind of 'picture':\n")
print_picture(plus_number,dash_number)
# print('\n')
print('\nAnd now comes some information about some people:')
print_file(file_name)