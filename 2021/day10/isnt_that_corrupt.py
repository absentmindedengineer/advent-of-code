import copy
with open('day10/chunks.txt','r') as f:
    subsystem_raw_data = f.readlines()
    data_lst = []
    for line in subsystem_raw_data:
        data_lst.append(list(line))


left_symbols = ['(', '[', '<', '{']
right_symbols = [')', ']', '>', '}']
value_symbols = [ 3,  57, 1197, 25137]

corrupted_values = dict() #first value is row number and second is value

test_lst = copy.deepcopy(data_lst)
for row in range(len(test_lst)):
    dynamic_symbol_lst = []
    for symbol in test_lst[row]:
        #different lengths for each line.
        
        if right_symbols.count(symbol) > 0:
            idx = right_symbols.index(symbol)
            #cannot (hope not) start with a right symbol
            if dynamic_symbol_lst[-1] == left_symbols[idx]:
                #the last symbol in dynamic_symbol_lst is the left equivalent of the examined symbol. Therefore we pop this value and remove the right version from the original list by simply exiting this iteration.
                dynamic_symbol_lst.pop()
                test_lst[row].pop(0)

            else:
                #we found a ful fisk. Here we found a different right symbol than is correct ->corrupt line. Store the value.
                corrupted_values[symbol] = value_symbols[idx]
                # mysterious error if you use row + value_symbols[idx]


            #we found a right symbol!
            #find the leftmost buddy. If it's a mismatch we jump
            #out of here and save.

        else:
            dynamic_symbol_lst.append(test_lst[row].pop(0))            
        
print(sum(corrupted_values.values()),'\n', corrupted_values)
        
        