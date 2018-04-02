# -*- coding:utf-8 -*-  
#!/usr/bin/python
# in a function, we do not want to use return, instead we may want to sue generator
def f(n):
	"""
	the yield enables a function to comeback where it left off when it called again,
	this is the critical difference from a regular, a regular function can not comes
	back where it left off, the yield keyword helps a function to remember its state
	:param n:
	:return:
	"""

	for x in range(n):
		yield x**3

# another example of using yield
# build the primes() function so that i fills the n one at a time, and come back to primes() function
# until n > 100
def isPrime(n):
	if n == 1:
		return False
	for t in range(2,n):
		return False
	return True
def primes(n = 1):
	while n < 100:
		if isPrime(n):yield n
		n += 1

#