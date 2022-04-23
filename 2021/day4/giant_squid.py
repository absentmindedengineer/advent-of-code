bin_lst=[]
with open('day4/bingo.txt','r') as f:
    lines = f.readlines()
    for element in lines:
        bin_lst.append(element.strip())
        if element == "":
            break

read_up_lst= []
bingo_boards = []

with open('day4/bingo.txt','r') as f:
    line = f.readline()
    for element in line:
        read_up_lst.append(element.strip())
    remaining_lines = f.readlines()
    for element in remaining_lines:
        bingo_boards.append(element.strip())
    

print(bingo_boards)

