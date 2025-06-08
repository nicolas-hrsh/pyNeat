# Optimize the code below

# results = []  
# for num in range(1, 1000000):  
#     results.append(num ** 2)  

# The code goes from 1 to 1000000 and raises every number to power of 2 and saves in the list.

results = (num ** 2 for num in range(1, 1000000)) 

# make it memory efficient by not using list but generator expression

