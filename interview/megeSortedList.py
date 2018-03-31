# merging two sorted list
# have two sorted list, and we want to write a function to merge the two list into one sorted list
a = [3,4,10,11,18]
b = [1,5,7,12,13,19,21]

# method1
def method1():
	c = []
	while a and b:
		if a[0] < b[0]:
			c.append(a.pop(0))
		else:
			c.append(b.pop(0))
	return c + a + b

def method2():
	a = [3,4,10,11,18]
	b = [1,5,7,12,13,19,21]
	a.extend(b)
	c = sorted(a)
	return c

if __name__ == '__main__':
	print(method1())
	print(method2())
