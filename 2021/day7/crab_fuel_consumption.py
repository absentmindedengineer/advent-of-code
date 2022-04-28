import statistics
"""
For optimal position x* the crabs fuel consumption is minimal meaning
d/dx(x*) = 0.
"""

crab_pos=[]
coordinate_data = []
with open('day7/crab_position.txt','r') as f:
    remaining_lines = f.readlines()
    for element in remaining_lines:
        coordinate_data.append(element.strip(''))

for idx in range(len(coordinate_data)):
    grr=coordinate_data[idx].split(",")
for i in range(len(grr)):
    crab_pos.append(int(grr[i]))

mean = statistics.mean(crab_pos)
cost_fcn1 = [0]*1000

for j in range(0,1000):
    for i in range(len(crab_pos)):
        cost_fcn1[j]+=abs(j-crab_pos[i])
print(f"Part1) {min(cost_fcn1)}")

cost_fcn2 = [0]*1000
for j in range(0,1000):
    for i in range(len(crab_pos)):
        n = abs(crab_pos[i]-j)
        cost_fcn2[j] += n*(n+1)/2

print(f"Part2) {min(cost_fcn2)}")
