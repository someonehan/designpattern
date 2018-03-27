
class error(Exception):pass
		
class Stack:
	"""docstring for Stack"""
	def __init__(self, stack = []):
		self.stack = []
		for x in stack:self.push(x)

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if self.empty():raise error('empty')
		return self.stack.pop()

	def top(self):
		return self.stack[-1]

	def empty():
		return not self.stack

	def __len__(self):
		return len(self.stack)

	def __getitem__(self, index):
		return self.stack[index]