# -*- coding:utf-8 -*-  
#!/usr/bin/python
# builder pattern

"""
意图：将一个复杂对象的构建和它的表示分离，使得同样的构建过程可以创建不同的表示
适用：1. 创建复杂对象的算法应该独立于该对象的组成部分以及他们的装配方式
	 2. 当构造过程必须允许被构造的对象有不同的表示
模式组成：
抽象建造者：为创建一个product对象的各个部分指定抽象接口，以规范产品对象的各个组成成分建造，一般而言，此角色规定要实现
复杂对象的哪些部分的创建，并不涉及具体的对象部件的创建
具体建造者: 实现builder接口以构造和装配该产品的各个部件，及实现建造者builder的方法
	    定义并明确它所创建的表示，即针对不同的商业逻辑，具体化复杂对象的各个部分的创建
	    提供一个检索产品的接口
	    构造一个使用builder接口的对象即在指导者的调用下创建产品实例
指导者：调用具体建造角色以创建产品对象的各个部分，指导者并没有涉及到具体产品类的信息，真正拥有具体产品信息有具体建造者提供
它只负责保证对象各个部分完整创建或按照某种顺序创建
产品角色：建造者的复杂对象他要包含那些定义组件的类，包括将这些组件装配成产品的接口
"""
from abc import ABCMeta, abstractmethod

class BasicBuilder(metaclass=ABCMeta):
	@abstractmethod
	def build_head(self):
		pass

	@abstractmethod
	def build_body(self):
		pass

	@abstractmethod
	def build_hand(self):
		pass

	@abstractmethod
	def build_foot(self):
		pass

class commonPersonBuilder(BasicBuilder):
	def build_head(self):
		print('common build head')
	def build_body(self):
		print('common build body')
	def build_foot(self):
		print('common build foot')
	def build_hand(self):
		print('common build hand')

class RobotPersonBuilder(BasicBuilder):
	def build_head(self):
		print('Robot build head')
	def build_body(self):
		print('Robot build body')
	def build_hand(self):
		print('Robot build hand')
	def build_foot(self):
		print('Robot build foot')

class Person:
	def __init__(self, heads, bodys, hands, foots):
		self.heads = heads
		self.bodys = bodys
		self.heads = hands
		self.foots = foots
	def __str__(self):
		return 'Person with {0} heads'.format(len(self.heads))

	def __repr__(self):
		return 'Person with {0} heads'.format(len(self.heads))

	__str__ = __repr__

class PersonDirector:
	def __init__(self, builder):
		self.builder = builder

	def create_person(self, headnum, bodynum, handnum, footnum):
		p = Person
		p.heads = [self.builder.build_head() for i in range(headnum)]
		p.bodys = [self.builder.build_body() for i in range(bodynum)]
		p.hands = [self.builder.build_hand() for i in range(handnum)]
		p.foots = [self.builder.build_foot() for i in range(footnum)]
		return p

if __name__ == '__main__':
	builder = commonPersonBuilder()
	pd = PersonDirector(builder)
	per = pd.create_person(3, 4,5,6)
	print(str(per))

