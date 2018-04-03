# -*- coding:utf-8 -*-  
#!/usr/bin/python
# Bridge 桥接模式

"""
意图：         将一组实现与另一组使用它们的对象分离
问题：         一个抽象类的派生类必须使用多个实现，但不能够出现类数量爆炸性增长
解决方案：     为所有实现定义一个接口，供抽象类的所有派生类使用
参与者与协作者：Abstraction为所要实现的对象定义接口，Implementor为具体的实现类定义接口，Abstraction
             的派生类使用Implementor的派生类，却无需知道自己具体使用的是哪一个ConcreteImplementor
效果：        实现和使用实现的对象解o，
实现：        1. 将实现封装在抽象类中
             2. 在要实现的抽象类中提供一个包含实现的句柄
"""
import collections
from abc import ABCMeta
import Image


def has_method(*methods):
	"""
	定义带有参数的装饰器
	http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p04_define_decorator_that_takes_arguments.html
	"""
	def decorator(Base):
		def __subclasshook__(Class, Subclass):
			"""
			当调用isinstance方法的时候会调用第二个参数的__subclasshook__方法
			"""
			if Class is Base:
				attritubes = collections.ChainMap(*(Supserclass.__dict__ for Supserclass in Subclass.__mro__))

			if all(method in attritubes for method in methods):
				return True
			return NotImplemented
		Base.__subclasshook__ = classmethod(__subclasshook__)
		return Base
	return decorator

class BarCharter:
	def __init__(self, renderer):
		if not isinstance(renderer, BarRender):
			raise TypeError("excepted object of BarRender {}".format(type(renderer).__name__))
		self._renderer = renderer
	def render(self, caption, pairs):
		maximun = max(value for _, value in pairs)
		self._renderer.initialize(len(pairs), maximun)
		self._renderer.draw_caption(caption)
		for name,value in pairs:
			self._renderer.draw_bar(name,value)
		self._renderer.finalize()

@has_method('initialize', 'draw_caption', 'draw_bar','finalize')
class BarRender(metaclass=ABCMeta):pass

class TextBarRender():
	def __init__(self, scaleFactor=40):
		self.scaleFactor = scaleFactor

	def initialize(self, bars, maxinum):
		assert bars > 0 and maxinum > 0
		self.scale = self.scaleFactor / maxinum

	def draw_caption(self, caption):
		print('{0:^{2}}\n{1:^{2}}'.format(caption, '='*len(caption), self.scaleFactor))

	def draw_bar(self, name, value):
		print('{}{}'.format('*'*int(value*self.scale),name))

	def finalize(self):
		pass

class ImageBarRender():
	"""
	调用Image库来来绘制
	"""
	def __init__(self, stepHeight=10, barWidth=30, barGap=2):
		self.stepHeight = stepHeight
		self.barWidth   = barWidth
		self.barGap     = barGap

	def initialize(self, bars, maxinum):
		assert bars > 0 and maxinum > 0

		self.index = 0

	def draw_caption(self, caption):
		pass

	def draw_bar(self, name ,value):
		pass

	def finalize(self):
		pass


def main():
	pairs = {('Mon',16),('Tue', 19),('Wed',12),('Thu',3)}
	textBarChart = BarCharter(TextBarRender())
	textBarChart.render('Forecast 4/5', pairs)

if __name__ == '__main__':
    main()