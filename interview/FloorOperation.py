# write a floor division function without using '/' or '%' operator

def floor(a,b):
	count = 0
	sign = 1 if a > 0 else -1
	while True:
		if b == 1:
			return a
		if a >= 0:
			if a > 0:
				a -= b
				if a < 0:break
			else:
				a = -a - b
				a = -a
				if a > 0:
					count += 1
					break
			count += 1
		else:
			return 0

	return count * sign



if __name__ == '__main__':
	print(floor(1,2)) #0
	print(floor(2,1)) #2