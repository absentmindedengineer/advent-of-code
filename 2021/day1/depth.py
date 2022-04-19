#day1 2021 
with open('data.txt', 'r') as f:
    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]


prev_entry = measurements[0]
increases = 0
for entry in measurements[1:]:
    if entry > prev_entry:
        increases += 1
    prev_entry = entry

increased = 0
for i in range(len(measurements)-1):
        if measurements[i+1] > measurements[i]:
            increased +=1
print(increases, increased)

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
    if measurements[idx+3] > measurements[idx]:
        pretty_window_increase += 1

print(window_increase, pretty_window_increase)



###############################################################################
# Takeaways:

#1. Using elements in the list instead of the list index and counting up. It's
# different and not at first kind of unintuitive.

#2 The indexing system in python is fubar.
#lst[0] is first element
#idx[0:1] is also the first element
#idx[0:2] is first and second
#idx[2] is the third element.

#3 Using something as below does not work at all despite looking very similar. 
# at first it was off by one increase with the correct logic. 

# This creates something incorrectly?
# with open('/home/gardson/absentminded/advent-of-code/2021/day1/data.txt','r') as f:
#     depth_lst = f.readlines()
#     #depth_lst = [line.strip() for line in f]
# pass

# print(len(depth_lst)) #same length
# print(len(depth_lst[1])) #this is just nonsense
# print(sum(depth_lst)) #sum cannot use this list as it is int+str
