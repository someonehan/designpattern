# fetch every other item in list

L = [l*10 for l in range(5)]
print(L)


def method1():
	for i,v in enumerate(L):
		if i % 2 == 0:
			print v


if __name__ == '__main__':
	method1()