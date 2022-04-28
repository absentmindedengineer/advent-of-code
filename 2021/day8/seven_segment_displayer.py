
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

counter=0
for i in range(len(tmp_lst)):
    for j in range(4):
        length = len(tmp_lst[i][j])
        if length in [2,3,4,7]:
            counter+=1
        else:
            pass
        # match length: #sad python3.8 noises
        #     case 1:
        #         counter+=1
        #     case 3:
        #         counter+=1
        #     case 7:
        #         counter+=1
        #     case 8:
        #         counter+=1

print(counter)