import os

# INSERT YOUR CODE HERE

letters='ABCDEFGH'
dictionary = 'dictionary.txt'
solutions = []

# INSERT YOUR CODE HERE
length_dict={}
letters_list=sorted(list(letters))
len_letters=len(letters)
with open(dictionary,'r') as file:
    data=file.readlines()
    for item in data:
        if len(item)<len_letters:
            if not length_dict[len(item)]:
                length_dict[len(item)]=[item]
            else:
                length_dict[len(item)].append(item)
file.close()
for i in range(1,len(letters)+1):
    for item1 in length_dict[i]:
        for item2 in length_dict[]







if not solutions:
    print('There is no solution.')
else:
    print(f'The pairs of words using all (distinct) letters '
          f'in "{letters}" are:'
         )
    for solution in solutions:
        print(solution)