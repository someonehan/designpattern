# in information theory, the hamming distance between two strings of equal length is the number
# of positions at which the corresponding symbols are different
def hamming(s1,s2):
	if len(s1) != len(s2):
		raise ValueError("Not defined unequal length sequences")

	return sum(c1 != c2 for c1,c2 in zip(s1,s2))

if __name__ == '__main__':
	print(hamming('123456','122456'))