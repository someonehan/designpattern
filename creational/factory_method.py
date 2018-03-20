# -*- coding:utf-8 -*-  
#!/usr/bin/python
# factory_method pattern

"""
工厂方法
意图：定义一个用于创建对象的接口，让子类决定实例化哪一个类，factorymethod使一个类的实例化延迟到子类
适用：当一个类不知道它所必须创建的对象的类的时候
      当一个类希望它的子类来指定它所创建的对象的时候
      当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类代理者这一信息局部化的时候
"""

from abc import abstractmethod, ABCMeta

BLACK, WHITE = ('BLACK', 'WHITE')

class AbstractBoard(metaclass=ABCMeta):
	def __init__(self, rows, columns):
		self.board = [[None for _ in range(columns)] for _ in range(rows)]
		self.populate_board()
	@abstractmethod
	def populate_board(self):
		pass

	def __str__(self):
		squares = []
		for y, row in enumerate(self.board):
			for x, piece in enumerate(row):
				square = console(piece, BLACK if (x + y) % 2 else WHITE)
			squares.append(square)
		return "".join(squares)

class CheckersBoard(AbstractBoard):
	def __init__(self):
		super().__init__(10, 10)

	def populate_board(self):
		for x in range(0, 9, 2):
			for y in range(4):
				column = x + ((y + 1) % 2)
				for row, color in ((y, 'black')(y + 6, 'white')):
					self.board[row][column] = self.create_piece('draught', color)
					
	def create_piece(self, kind, color):
		if kind == 'draught':
			return eval("{}{}()".format(color.title(), kind.title()))

class Piece(str):
	__slots__ = ()


class BlackDraught(Piece):
	def __init__(self):
		pass

class WhiteDraught(Piece):
	def __init__(self):
		pass