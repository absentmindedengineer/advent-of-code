#fuel_consumption

import statistics

from sklearn.cluster import k_means

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

lol = [0]*1000

for _ in range(0,1000):
    for i in range(len(crab_pos)):
        lol[_]+=abs(_-crab_pos[i])

#print(lol)
#print(min(lol))


cost_fcn = [0]*1000
for x_star in range(0,1000):
    for i in range(len(crab_pos)):
        n = abs(crab_pos[i]-x_star)
        cost_fcn[x_star] += n*(n+1)/2

print(min(cost_fcn))
