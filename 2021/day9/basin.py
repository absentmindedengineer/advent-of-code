lst_2d_height = []
with open('day9/height_map.txt','r') as f:
    tmp_h = f.readlines()
    for element in tmp_h:
        lst_2d_height.append([int(elem) for elem in list(element.strip())])

basin_basin = lst_2d_height
for v in range(len(basin_basin)):
        basin_basin[v][:] = [True]*len(basin_basin[v])

low_point_heights = []
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



print(f"risk level: {sum(low_point_heights)+len(low_point_heights)}")

