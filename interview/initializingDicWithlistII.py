# we want to make a dictionary with the number of digits as the key and list of the numbers the values
L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

from collections import defaultdict

d = defaultdict(list)
for num in L:
	d[len(str(num))].append(num)

print(d)