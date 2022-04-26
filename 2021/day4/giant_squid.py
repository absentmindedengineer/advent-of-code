import re
import numpy as np

bin_lst=[]
board_sz = 5
read_up_lst= []
bingo_boards = []

with open('day4/bingo.txt','r') as f:
    line = f.readline()
    read_up_lst = list((line.rstrip()).split(','))
    
    remaining_lines = f.readlines()
    for element in remaining_lines:
        bingo_boards.append(element.strip())
    

for item in range(len(bingo_boards)):
    bin_lst.append(re.findall(r'\S+', bingo_boards[item]))

raw_string_lst = [value for value in bin_lst if value != []]

board_lst=[]
for board in range(len(raw_string_lst)):
    for column in range(board_sz):
        board_lst.append(raw_string_lst[board][column])



#logic:
""" 
We deal with one board at a time.
1. we draw a value from the read_up_lst.
1.1 we iterate over all items and set them to None, 'X' or something else.

2.1 Select a bingo board.
2.2 To check if Bingo has happened we check if a all values in a row
are equal to the set value. This is done five times for each board.
Similarly we do this for the five columns.
"""



def function_find_board_and_drawn_number(board_lst, read_up_lst, board_sz):
    for read_up_item in read_up_lst:
        #this read_up_item is a string.

        board_lst = list(map(lambda x: None if x == read_up_item else x, board_lst))
        #board updated
        print(board_lst)
        for board in range(int(len(board_lst)/(board_sz*board_sz))):
            for count in range(board_sz):

                board_start = board*board_sz*board_sz
                idx_col = list(range(board_start+count, board_start+board_sz*board_sz+count, board_sz))
                idx_row = list(range(board_start+count*board_sz, board_start+(count+1)*board_sz))#board*board_sz*board_sz + count*board_sz
                
                if [None]*board_sz == [board_lst[x] for x in idx_row]:
                    print(f'lateral bingo on board number: {board}. \
                        after {read_up_lst.index(read_up_item)} drawn numbers with number\
                        {read_up_item}')
                    return board_lst, board, int(read_up_item)

                if [None]*board_sz == [board_lst[x] for x in idx_col]:
                    print(f'vertical bingo on board number: {board},\
                        after {read_up_lst.index(read_up_item)} drawn numbers with number\
                        {read_up_item}.')
                    return board_lst, board, int(read_up_item)

bingo_boards_final, board_bingo, number_drawn = function_find_board_and_drawn_number(board_lst, read_up_lst, board_sz)

sum_of_not_picked=0
for iter in range(board_sz*board_sz):
    if bingo_boards_final[board_bingo*board_sz*board_sz+iter] != None:
        sum_of_not_picked += int(bingo_boards_final[board_bingo*board_sz*board_sz+iter])
        print(int(bingo_boards_final[board_bingo*board_sz*board_sz+iter]))
    elif bingo_boards_final[board_bingo*board_sz*board_sz+iter] == None:
        pass
    else:
        print("logic error.")

print(f'Answer: Bingo board: {board_bingo} with a remaining sum of: {sum_of_not_picked},\
    with number {number_drawn} resulting in the result of: {number_drawn*sum_of_not_picked}')