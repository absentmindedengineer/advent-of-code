# power consumption:
# gamma_rate*epsilon_rate.
import itertools
import numpy as np

bin_lst = []
with open('day3/binary_data.txt','r') as f:
    lines = f.readlines()
    for element in lines:
        bin_lst.append(element.strip())
    #lines = f.readlines()
    #bin_lst = [int(entry.strip()) for entry in lines]
    #this requires a different solution as you are handling pure integers
    #instead of strings which can be indexed easily with [i].


gamma_rate=None
epsilon_rate=None



word_length = len(bin_lst[0]) #remove line
compare_length = len(bin_lst)/2 #the counter doesn't have to count both 0's and
                              #1's. it can count a single one and compare with
                              #the length
sum_each_binary = [0]*word_length
for i in range(len(bin_lst)):
    for j in range(word_length):
        sum_each_binary[j] += int(bin_lst[i][j]) #if zero unchanged



majority_vote_binary = [0]*word_length
for i in range(word_length):
    if sum_each_binary[i] > compare_length:
        majority_vote_binary[i] = 1
    else:
        majority_vote_binary[i] = 0
        #not necessary, but good for readability.


nmbr = ''.join(str(x) for x in majority_vote_binary)
binary_number=int(nmbr)

print(f"thus the binary number is: {binary_number}")
zeros_nmbr = nmbr # we are interested in modifying this list to calculate the 
                  # other value. 


binary_number_flipped = 0
for i in range(word_length):
    if nmbr[i] == '0':
        binary_number_flipped += pow(10,word_length-1-i)
    elif nmbr[i] == '1':
        binary_number_flipped += 0*pow(10,word_length-1-i)
        #adding nothing of value is what I excel at.
    else:
        print('Error: Expected values inside string to be either one or zero.')
print("zero_number_bin", binary_number_flipped)


print(f"The number and its counterpart should be all ones:\
     {binary_number+binary_number_flipped}")

gamma_rate = int(str(binary_number),2)
epsilon_rate = int(str(binary_number_flipped),2)

power_consumption = gamma_rate*epsilon_rate

print(f"power consumption: {power_consumption}")


