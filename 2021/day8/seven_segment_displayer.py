import re

tmp_lst = []
coordinate_data = []
with open('day8/abcdefg_data.txt','r') as f:
    remaining_lines = f.readlines()
    for element in remaining_lines:
        coordinate_data.append(element.strip())

idx_line = coordinate_data[0].find('|')
for i in range(len(coordinate_data)):
    string_of_four = coordinate_data[i][idx_line+2:]
#    for j in range(4):
    tmp_lst.append(string_of_four.split(' '))

print(tmp_lst)
#print(coordinate_data)