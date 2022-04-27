initial_fish_lst = []
with open('day6/initial_fish_state.txt','r') as f:
    line = f.readline()
    tmp_str_lst = list(line.split(','))
for i in range(len(tmp_str_lst)):
    initial_fish_lst.append(int(tmp_str_lst[i]))


fish_lst = initial_fish_lst
fish_bool_lst = [False]*len(fish_lst)


#fish_lst = [3,4,3,1,2]

for _ in range(80):
    if len(fish_lst) > 300:
        print(fish_lst[298:305])
    for item in range(len(fish_lst)):    
    #logic
        if fish_lst[item] >= 1 and fish_lst[item] <= 8:
            fish_lst[item]-=1
        elif fish_lst[item] == 0:
            fish_lst[item] = 6
            fish_lst.append(8)

print(len(fish_lst))    