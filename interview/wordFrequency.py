# Get word frequency-initializing dictionary
# two way to solving word frequency problem
def method1():
	"""
	using the fromkeys method
	"""
	ss = "i figured it out I figured it out from black and white seconds and hours Maybe they had to take some time"
	word = ss.split()
	d = {}.fromkeys(word,0)
	for w in word:
		d[w] += 1
	print(d)

def method2():
	"""

	"""
	ss = "i figured it out I figured it out from black and white seconds and hours Maybe they had to take some time"
	d = {}
	for w in ss.split():
		d[w] = d.get(w,0) + 1
	print(d)

if __name__ == '__main__':
	method1()
	method2()