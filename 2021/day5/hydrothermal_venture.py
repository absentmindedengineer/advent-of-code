import re
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
    # line = f.readlines()
    # read_up_lst = list((line.rstrip()).split('->'))
    
    remaining_lines = f.readlines()
    for element in remaining_lines:
        coordinate_data.append(element.replace(' -> ',',').strip())

coordinate_data = [n.strip() for n in coordinate_data]
""" Idea is to have a bunch of lists and compare their four coordinates to 
eachother and see whether they should be placed in this new data place or not."""

tmp_lst = []
horizontal_or_vertical_data = []
horizontal_or_vertical_bool_data = []

for idx in range(len(coordinate_data)):
    tmp_lst.append(coordinate_data[idx].split(","))


# horizontal_or_vertical_data consists of lists with four elements.

for idx in range(len(tmp_lst)):
    if tmp_lst[idx][0] == tmp_lst[idx][2]:
        #vertical 
        horizontal_or_vertical_data.append(tmp_lst[idx])
        horizontal_or_vertical_bool_data.append('vertical')
    if tmp_lst[idx][1] == tmp_lst[idx][3]:
        #horizontal
        horizontal_or_vertical_data.append(tmp_lst[idx])
        horizontal_or_vertical_bool_data.append('horizontal')
    else:
        pass
        #not horizontal or vertical.

field = np.zeros((1000,1000), dtype=int)

for line in range(len(horizontal_or_vertical_data)):
    # Since they are horizontal or vertical it's just as good to decide which it is.
    if horizontal_or_vertical_bool_data[line] == 'vertical':
        x_pos = int(horizontal_or_vertical_data[line][0])
        #range is so fucking stupid.
        tmp_lst2 = sorted([int(horizontal_or_vertical_data[line][1]), int(horizontal_or_vertical_data[line][3])])
        for y_pos in range(tmp_lst2[0],tmp_lst2[1]+1): 
            field[x_pos, y_pos]+=1

    elif horizontal_or_vertical_bool_data[line] == 'horizontal':
        y_pos = int(horizontal_or_vertical_data[line][1])
        tmp_lst3 = sorted([int(horizontal_or_vertical_data[line][0]), int(horizontal_or_vertical_data[line][2])])
        for x_pos in range(tmp_lst3[0],tmp_lst3[1]+1):
            field[x_pos, y_pos]+=1
    else:
        print("logic error")

print(field[np.where(field > 1)].shape)