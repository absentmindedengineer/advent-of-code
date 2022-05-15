import copy

#file_handling
with open('day10/chunks.txt','r') as f:
    subsystem_raw_data = f.readlines()
    data_lst = []
    for line in subsystem_raw_data:
        data_lst.append(list(line))
constant_lst = copy.deepcopy(data_lst)


left_symbols = ['(', '[', '<', '{']
right_symbols = [')', ']', '>', '}']
value_symbols = [ 3,  57, 25137, 1197]

corrupted_values = []
remove_lines = []

for row in range(len(data_lst)):
    dynamic_symbol_lst = []
    for symbol in constant_lst[row]:
        #have a constant list to get values from and another to pop from. Symbol doesn't simply behave as one would want it to just fetch the value after the one it just got if you modify the list, here by popping.

            if symbol in right_symbols:
                #how many times does the value of symbol occur in right symbols.
                idx = right_symbols.index(symbol)

                if dynamic_symbol_lst[-1] == left_symbols[idx]:
                    #the last symbol in dynamic_symbol_lst is the left equivalent of the examined symbol. Therefore we pop this value and remove the right by popping it from the original list as well.

                    #We only need to examine the first values as we are popping the other 'couple' values. Meaning that there are no right symbols to look at.

                    dynamic_symbol_lst.pop()
                    data_lst[row].pop(0)
                    
                else:
                    #we found a ful fisk. Here we found a different right symbol than is correct -> corrupt line. Store the value.
                    corrupted_values.append(value_symbols[idx])
                    
                    #this leaves the current row if line is corrupted.
                    remove_lines.append(row)
                    break 
                    
            else:
                dynamic_symbol_lst.append(data_lst[row].pop(0))            
print(f'Total syntax error score: {sum(corrupted_values)}')
##

incomplete_lst = copy.deepcopy(constant_lst)
for row in range(len(constant_lst)):        
    incomplete_lst[row] = ''.join(incomplete_lst[row])
for index in sorted(remove_lines, reverse=True):
    #you need to delete them in reverse order so that you don't throw off the subsequent indexes.
    del incomplete_lst[index]


# write to file, not necessary though.
incomplete_file = open('day10/incomplete_list.txt','w')
for row in incomplete_lst:
    incomplete_file.write(row)


