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


def has_method(*methods):
	"""
	定义带有参数的装饰器
	http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p04_define_decorator_that_takes_arguments.html
	"""
	def decorator(Base):
		def __subclasshook__(Class, Subclass):
			if Class is Base:
				attritubes = collections.ChainMap(*(Supserclass.__dict__ for Supserclass in Subclass.__mro__))

			if all(method in attritubes for method in methods):
				return True
			return NotImplemented
		Base.__subclasshook__ = classmethod(__subclasshook__)
		return Base
	return decorator