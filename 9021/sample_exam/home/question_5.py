# Will be tested with year between 1913 and 2013.


import csv
import os

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',\
             'Sep', 'Oct', 'Nov', 'Dec']
    # INSERT YOUR CODE HERE
    the_months = []
    # dir_name = os.getcwd()
    # csv_file_name = str(dir_name) + '/cpiai.csv'
    csv_file_name='cpiai.csv'
    detail_dict = {}
    with open(csv_file_name, 'r') as csv_file:
        data = csv_file.readlines()
        data.pop(0)
        for item in data:
            date, index, inflation = item.split(',')
            inflation = inflation[:-1]
            year_of_date, mon_of_date, date_of_date = date.split('-')
            detail_dict[(year_of_date, mon_of_date)] = inflation
    csv_file.close()
    inflation_result = []
    all_result = {}
    for key, values in detail_dict.items():
        if int(key[0]) == year:
            inflation_result.append(float(values))
            all_result[key] = float(values)
    max_inflation = max(inflation_result)

    for key, values in all_result.items():
        if values == max_inflation:
            year_all_result, month_all_result = key[0], key[1]
            the_months.append(months[int(month_all_result) - 1])
    print(f'In {year}, maximum inflation was: {max_inflation}')
    print('It was achieved in the following months:', end='')
    the_num_of_months = len(the_months)
    for i in range(len(the_months)):
        if i == 0:
            putout = ' ' + the_months[i]
            print(putout, end='')
        else:
            putout = ', ' + the_months[i]
            print(putout, end='')






if __name__ == '__main__':
    import doctest
    doctest.testmod()
