import numpy as np
"""
Avoid Hydrothermal vent lines. Lines are defined as x1,y1->x2,y2.
Initially consider only horizontal & veritcal lines.
i.e. x1=x2 or y1=y2.

These are "blocks" which means if a point exits on a line
p:{x_i,y_i} that point will have the value of 1. If an additional line exists
on that point, we add +1 to that point.

Part1: Count the number of points which has values >=2.
"""

coordinate_data = []
with open('day5/vent_lines.txt','r') as f:
    remaining_lines = f.readlines()
    for element in remaining_lines:
        coordinate_data.append(element.replace(' -> ',',').strip())

coordinate_data = [n.strip() for n in coordinate_data]
""" Idea is to have a bunch of lists and compare their four coordinates to 
eachother and see whether they should be placed in this new data place or not."""

tmp_lst = []
line_data = []
line_bool_data = []

for idx in range(len(coordinate_data)):
    tmp_lst.append(coordinate_data[idx].split(","))

for idx in range(len(tmp_lst)):
    for iter in range(4):
        tmp_lst[idx][iter] = int(tmp_lst[idx][iter])

# line_data consists of lists with four elements.

for idx in range(len(tmp_lst)):
    if tmp_lst[idx][0] == tmp_lst[idx][2]:
        #vertical 
        line_data.append(tmp_lst[idx])
        line_bool_data.append('vertical')
    elif tmp_lst[idx][1] == tmp_lst[idx][3]:
        #horizontal
        line_data.append(tmp_lst[idx])
        line_bool_data.append('horizontal')
    elif abs(tmp_lst[idx][0]-tmp_lst[idx][2]) == abs(tmp_lst[idx][1]-tmp_lst[idx][3]):
        #diagonal
        line_data.append(tmp_lst[idx])
        line_bool_data.append('diagonal')
    else:
        pass
        #not horizontal or vertical.

field_diag = np.zeros((1000,1000), dtype=int)

for line in range(len(line_data)):
    # Since they are horizontal or vertical it's just as good to decide which it is.
    if line_bool_data[line] == 'vertical':
        x_pos = int(line_data[line][0])
        #range is so fucking stupid.
        y_lst = sorted([int(line_data[line][1]), int(line_data[line][3])])
        for y_pos in range(y_lst[0],y_lst[1]+1): 
            field_diag[x_pos, y_pos]+=1
    elif line_bool_data[line] == 'horizontal':
        y_pos = int(line_data[line][1])
        x_lst = sorted([int(line_data[line][0]), int(line_data[line][2])])
        for x_pos in range(x_lst[0],x_lst[1]+1):
            field_diag[x_pos, y_pos]+=1
    elif line_bool_data[line] == 'diagonal':
        #take the min_x, use the corresponding y-value
        #and find out if u wanna decrease the y-value or not.
        if line_data[line][0] < line_data[line][2]:
            x_range = range(line_data[line][0], line_data[line][2]+1)
        else:
            x_range = range(line_data[line][0],line_data[line][2]-1,-1)
        if line_data[line][1] < line_data[line][3]:
            y_range = range(line_data[line][1],line_data[line][3]+1)
        else:
            #assuming no zero length stuff.
            y_range = range(line_data[line][1],line_data[line][3]-1,-1)
        
        for idx in range(len(x_range)):
            #if it's diagonal it has the same length of x and y. this means we only
            #need one loop.
            x_pos = x_range[idx]
            y_pos = y_range[idx]
            field_diag[x_pos,y_pos] +=1


    else:
        print("logic error")

print(field_diag[np.where(field_diag >= 2)].shape)

counter = 0

for x in range(1000):
    for y in range(1000):
        if field_diag[x,y] > 1:
            counter+=1
print(counter)