class Stack:
	"""docstring for Stack"""
	def __init__(self, stack = []):
		self.stack = None
		for x in stack:self.push(x)

	def push(self, item):
		self.stack = item,self.stack

	def pop(self):
		node, self.stack = self.stack
		return node

	def empty(self):
		return not self.stack

	def __len__(self):
		len, tree = 0, self.stack
		while tree:
			len, tree = len + 1, self.stack[1]
		return len

	def __getitem__(self, index):
		len, tree = 0, self.stack
		while len < index and tree:
			len, tree = len + 1, self.stack[1]
		if tree:
			return tree[0]
		else:
			raise IndexError()

	def __repr__(self):
		return "Stack:{}".formate(self.stack)

if __name__ == '__main__':
	s = Stack([3,1,4,3,2,1,12])
	print(s.pop())
	s.push('hanxingzhi')
	print(s.pop())