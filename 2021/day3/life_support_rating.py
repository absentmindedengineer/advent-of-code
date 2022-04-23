from pyrsistent import discard


bin_lst = []
with open('day3/binary_data.txt','r') as f:
    lines = f.readlines()
    for element in lines:
        bin_lst.append(element.strip())

oxygen_binary_rating=None
carbon_dioxide_binary_rating=None

#multiply oxygen generator rating by c02 scrubber rating.

word_length=len(bin_lst[0])


discard_lst = bin_lst #discard_lst will get smaller as we discard
#based on bit criteria.
discard_c02_lst = bin_lst

for bit_pos in range(word_length):
    
    oxy_zero_lst=[]
    oxy_one_lst=[]

    
    c02_zero_lst=[]
    c02_one_lst=[]
    #These "list counters" are both useful for both c02 and oxygen, but the logic to determine
    #the list to go on is different.

    for word in range(len(discard_lst)):
        if discard_lst[word][bit_pos] == '1':
            oxy_one_lst.append(discard_lst[word]) 
            #store word, not bit value. length will determine comparison
        else:
            oxy_zero_lst.append(discard_lst[word])
    
    for word in range(len(discard_c02_lst)):
        if discard_c02_lst[word][bit_pos] == '1':
            c02_one_lst.append(discard_c02_lst[word]) 
        else:
            c02_zero_lst.append(discard_c02_lst[word])

    #Oxygen
    if len(oxy_one_lst) >= len(oxy_zero_lst):
        discard_lst=oxy_one_lst
    elif len(oxy_one_lst) < len(oxy_zero_lst):
        discard_lst=oxy_zero_lst
    else:
        print("logic error.")
        """In this case we always pick the value of the longest lst. so there's no need
        to correct this behaviour, unlike below. """


    #Carbon dioxide
    """We need these length comparisons to avoid trouble. Practically speaking I'm not sure
    what exactly is the case. However, if you have a discard_list of one value, this would
    give one of the lists length one and the other length 0. Thus, you pick the list with the
    least common number: the empty list and discard_c02_lst changes and you got nothing.
    
    Additionally this causes problems as we likely find the oxygen value but the if statement isn't
    gonna be true."""

    if len(c02_one_lst) >= len(c02_zero_lst) and len(discard_c02_lst)!=1:
        discard_c02_lst=c02_zero_lst
    elif len(c02_one_lst) < len(c02_zero_lst) and len(discard_c02_lst)!=1:
        discard_c02_lst=c02_one_lst
    else:
        pass 
        #we have found the value.

    
    if len(discard_lst) == 1 and len(discard_c02_lst) == 1:
        oxygen_binary_rating = int(discard_lst[0],2) # we don't need the first zeros.
        carbon_dioxide_binary_rating = int(discard_c02_lst[0],2) #keep it string as we can use int.
        print(discard_lst[0],discard_c02_lst[0])
        break 
    
print(oxygen_binary_rating, carbon_dioxide_binary_rating)
print(f"life support rating: {oxygen_binary_rating*carbon_dioxide_binary_rating}")