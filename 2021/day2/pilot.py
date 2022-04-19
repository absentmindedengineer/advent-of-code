#cmds: 
# forward 
# down
# up
#takes natural numbers

#initial position at horizontal x=0 and depth y=0.
# down[input] increases y
#   up[input] decreases y

from lib2to3.pytree import convert
import re

converted_list=[]
with open('day2/cmds.txt','r') as f:
    lines = f.readlines()
    for element in lines:
        converted_list.append(element.strip())
#measurements = [int(entry.strip()) for entry in lines]

print(type(converted_list[0]))

horizontal_length=0
vertical_depth=0

for i in range(len(converted_list)):
    str_element = converted_list[i]
    if(str_element.find('forward') != -1):
        forward_length = int(re.search(r'\d+', str_element).group())
        horizontal_length +=forward_length
    elif (str_element.find('down') != -1):
        vertical_depth+=int(re.search(r'\d+', str_element).group())
    elif (str_element.find('up') != -1):
        vertical_depth-=int(re.search(r'\d+', str_element).group())

print(f"horizontal length: {horizontal_length}, depth = {vertical_depth}")
print(f"multiplied: {horizontal_length*vertical_depth}")

