
# with open('/home/gardson/absentminded/advent-of-code/2021/day1/data.txt','r') as f:
#     depth_lst = f.readlines()
#     #depth_lst = [line.strip() for line in f]
# increased = 0
# for i in range(len(depth_lst)-1):
#     #print(depth_lst[i+1],depth_lst[i])
#         if depth_lst[i+1] > depth_lst[i]:
#             increased +=1
# print(increased)
# # last=0
# # for num in depth_lst:
# #     if last != 0:
# #         if num > last:
# #             increased += 1
# #     last = num
# # print(increased)

with open('/home/gardson/absentminded/advent-of-code/2021/day1/data.txt', 'r') as f:
    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]

prev_entry = measurements[0]
increases = 0
for entry in measurements[1:]:
    if entry > prev_entry:
        increases += 1
    prev_entry = entry

print(increases)

# part2
#first measurement will be
window_increase = 0

for idx in range(len(measurements)-2):
    old_mean = sum(measurements[idx:idx+3])
    new_mean = sum(measurements[idx+1:idx+4])
    if new_mean > old_mean:
        window_increase+=1


#alternatively a much prettier solution. Notice the need to change(!) the
# length of the loop.
pretty_window_increase=0
for idx in range(len(measurements)-3):
    if measurements[idx+3]>measurements[idx]:
        pretty_window_increase+=1

print(window_increase, pretty_window_increase)
