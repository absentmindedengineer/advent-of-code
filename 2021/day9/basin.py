from nis import match
import numpy as np

lst_2d_height = []
with open('day9/height_map.txt','r') as f:
    tmp_h = f.readlines()
    for element in tmp_h:
        lst_2d_height.append([int(elem) for elem in list(element.strip())])

def ok_step(y_pos,x_pos):
    # position values
    center = lst_2d_height[y_pos][x_pos] 
    if y_pos == 0:
        above = 10
    else:
        above = lst_2d_height[y_pos-1][x_pos]
    if y_pos == len(lst_2d_height)-1:
        below = 10
    else:
        below = lst_2d_height[y_pos+1][x_pos]
    if x_pos == 0:
        left = 10
    else:
        left = lst_2d_height[y_pos][x_pos-1]
    if x_pos == len(lst_2d_height[0])-1:
        right = 10
    else:
        right = lst_2d_height[y_pos][x_pos+1]
    
    # sum handling jumping into new positions in case the
    # if statements are true. 
    sum = 0
    if basin[y_pos][x_pos] == True:
        basin[y_pos][x_pos] = False #dont count the same tile twice.
        sum+=1
    if above < 9 and above > center: 
        #9 is a wall and the new tile needs to be larger
        #than the last, otherwise we would be moving back and forth
        #forever in electric dreams.
        sum += ok_step(y_pos-1,x_pos)
    if below < 9 and below > center:
        sum += ok_step(y_pos+1,x_pos)
    if left < 9 and left > center:
        sum+= ok_step(y_pos,x_pos-1)
    if right < 9 and right > center:
        sum+= ok_step(y_pos,x_pos+1)
    else:
        pass
        #we hit a wall
    return sum

basin = np.full((len(lst_2d_height), len(lst_2d_height[0])), True)

low_point_heights = []
basin_sum = []
for idx_v in range(len(lst_2d_height)):
    for idx_h in range(len(lst_2d_height[0])):
        above,below,left,right = 10,10,10,10
        # outside this map is set to higher than max val.
        # idx vertical and horizontal
        # look left, right, up or below.
        point_height = lst_2d_height[idx_v][idx_h]
        if idx_v != 0:
            above = lst_2d_height[idx_v-1][idx_h]
        if idx_v != len(lst_2d_height)-1:
            below = lst_2d_height[idx_v+1][idx_h]
        if idx_h != 0:
            left = lst_2d_height[idx_v][idx_h-1]
        if idx_h != len(lst_2d_height[0])-1:
            right = lst_2d_height[idx_v][idx_h+1]
        
        if point_height < above and point_height < below and point_height < left and point_height < right:
            low_point_heights.append(point_height)
            #while we have the coordinates for a confirmed
            #low point we calculate the basin.
            basin_sum.append(ok_step(idx_v, idx_h))

three_largest_basins = 1
for _ in range(3):
    three_largest_basins *= basin_sum.pop(basin_sum.index(max(basin_sum)))







print(f"risk level: {sum(low_point_heights)+len(low_point_heights)}")
print(f'basin_sum : {three_largest_basins}')
