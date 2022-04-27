fish_lst = []
with open('day6/initial_fish_state.txt','r') as f:
    line = f.readline()
    tmp_str_lst = list(line.split(','))
for i in range(len(tmp_str_lst)):
    fish_lst.append(int(tmp_str_lst[i]))



for _ in range(80):
    for item in range(len(fish_lst)):    
        if fish_lst[item] >= 1 and fish_lst[item] <= 8:
            fish_lst[item]-=1
        elif fish_lst[item] == 0:
            fish_lst[item] = 6
            fish_lst.append(8)

print(f"Amount of lantern fish after {_} days: {len(fish_lst)}")