fish_lst = []
with open('day6/initial_fish_state.txt','r') as f:
    line = f.readline()
    tmp_str_lst = list(line.split(','))
for i in range(len(tmp_str_lst)):
    fish_lst.append(int(tmp_str_lst[i]))

fish_num = [0]*9
for i in range(len(fish_lst)):
    fish_num[fish_lst[i]] +=1 

num_days = 256
for i in range(1,num_days+1):
    
    #this doesn't start at day0.
    #+1 to include the last day.

    fish_num_tmp = [0]*9
    fish_num_tmp[0:8] = fish_num[1:9]
    fish_num_tmp[8] = fish_num[0]
    fish_num_tmp[6] += fish_num[0]
    fish_num = fish_num_tmp

    #print(f'day: {i} : {fish_num}, with sum {sum(fish_num)}')

print(f"Amount of lantern fish after {num_days} days: {sum(fish_num)}")
