output_lst=[]
tmp_lst = []
coordinate_data = []
with open('day8/abcdefg_data.txt','r') as f:
    remaining_lines = f.readlines()
    for element in remaining_lines:
        coordinate_data.append(element.strip())

idx_line = coordinate_data[0].find('|')
for i in range(len(coordinate_data)):

    string_of_all = coordinate_data[i]
    string_of_outputs = coordinate_data[i][idx_line+2:]

#    for j in range(4):
    tmp_lst.append(string_of_all.split(' '))
    output_lst.append(string_of_outputs.split(' '))

for i in range(len(tmp_lst)):
    tmp_lst[i].remove('|')




one = [None]*len(output_lst)
four = [None]*len(output_lst)
seven = [None]*len(output_lst)
for line in range(len(tmp_lst)):
    for idx in range(len(tmp_lst[line])):
        if len(tmp_lst[line][idx]) == 2:
            one[line] = list(tmp_lst[line][idx])
        elif len(tmp_lst[line][idx]) == 3:
            seven[line] = list(tmp_lst[line][idx])
        elif len(tmp_lst[line][idx]) == 4:
            four[line] = list(tmp_lst[line][idx])
    
    #this loop should only cover the output.

output_number_as_str = ['']*len(output_lst)
for line in range(len(output_lst)):
    for word in output_lst[line]:
            
        if len(word) == 2:
            output_number_as_str[line]+='1'
        elif len(word) == 3:
            output_number_as_str[line]+='7'
        elif len(word) == 4:
            output_number_as_str[line]+='4'
        elif len(word) == 7:
            output_number_as_str[line]+='8'
        
        
        #here we see if the known numbers, such as seven, is a
        #substring of the output word. That's how we determine
        #the digit.


        elif len(word) == 5:
            #if seven in word:
            if all(char in word for char in seven[line]):
                output_number_as_str[line]+='3'
            else:
                sum_lst = [None]*len(four[line])
                for idx in range(len(four[line])):
                    if four[line][idx] in word:
                        sum_lst[idx] = 1
                    else:
                        sum_lst[idx] = 0
                
                if sum(sum_lst) == 3:
                    output_number_as_str[line]+='5'
                elif sum(sum_lst) == 2:
                    output_number_as_str[line]+='2'
                else:
                    print("logic error.")
            

        


        elif len(word) == 6:
            if all(char in word for char in four[line]):
                output_number_as_str[line]+='9'
            elif all(char in word for char in seven[line]):
                output_number_as_str[line]+='0'
            else:
                output_number_as_str[line]+='6'

sum_lst2 = []
for i in range(len(output_number_as_str)):
    sum_lst2.append(int(output_number_as_str[i]))

print(sum(sum_lst2))