
class error(Exception):pass		
class stack:
	def __init__(self, stack = []):
		self.stack = []
		for x in stack:self.push(x)
		self.stack.reverse()	
		

	def push(self, item):
		self.stack = [item] + self.stack

	def pop(self):
		if self.empty():
			raise error('empty stack')
		top,*self.stack = self.stack
		return top

	def empty(self):
		return not self.stack

	def __repr__(self):
		return 'Stack :{}'.formate(self.stack)

	def __eq__(self, other):
		return self.stack == other.stack

	def __len__(self):
		return len(self.stack)

	def __add__(self, other):
		return stack(self.stack + other.stack)

	def __mul__(self, args):
		return stack(self.stack * args)

	def __getitem__(self, offset):
		return self.stack[offset]

	def __getattr__(self, name):
		return getattr(self.stack, name)

if __name__ == '__main__':
	s = stack([1,2,3,4])
	print(s.pop())
	s.push(5)
	print(s.pop())
