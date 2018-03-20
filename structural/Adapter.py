# -*- coding:utf-8 -*-  
#!/usr/bin/python


"""
意图：将一个类的接口转化成客户希望另外一个接口，Adapter能够使用原本由于接口不兼容而不能一起工作的类可以一起工作
问题：系统的数据和行为都正确，但是接口不符合，通常用于必须从抽象类派生时
解决方案：Adapter模式提供具有所需接口的包装类
参与者和协作者：Adapter改变Adaptee的接口，使得Adaptee与Adapter的父类Target相匹配，这样Client就可以使用Adaptee了
效果：Adapter模式使得原有的对象能够适用于新的结构，不受其他接口的限制
"""


from abc import ABCMeta
import collections
import sys


class Page:
	def __init__(self, title, render):
		if not isinstance(render, Render):
			raise TypeError('需要Render类型给定：{}'.format(type(render).__name__))
		# assert isinstance(render, Render)
		self.title = title
		self.render = render
		self.paragraph = []

	def ren(self):
	    self.render.header('fad')
	    self.render.paragraph('fadfadsf')
	    self.render.footer()

class Render(metaclass=ABCMeta):
	@classmethod
	def __subclasshook__(cls, Subclass):
		"""
		特殊方法：__subclasshook__ python内置的isinstance方法需要通过这个方法来确定函数的首个参数
		是不是第二个参数的子类
		"""

		if cls is Render:
		    attributes = collections.ChainMap(*(SuperClass.__dict__ for SuperClass in Subclass.__mro__))
		    methods = ("header","paragraph","footer")
		    if all(method in attributes for method in methods):
		        return True
		return NotImplemented

class textRender:
	def __init__(self, width=80, file=sys.stdout):
		self.width = width
		self.file = file
		self.previous = False
	def header(self, title):
		self.file.write(title)
	def paragraph(self, text):
		if not self.previous:
			self.file.write("\n")
		self.file.write(text)
		self.previous = True
	def footer(self):
		pass

class htmlWriter:
	def __init__(self, file=sys.stdout):
		self.file = file

	def htmlheader(self, title):
		self.file.write(title)
	def htmlparagraph(self, text):
		self.file.write(text)
	def htmlfooter(self):
		pass

class htmlRender:
	def __init__(self, htmlwriter):
		self.htmlwriter = htmlwriter
	def header(self, title):
		self.htmlwriter.htmlheader(title)
	def paragraph(self, text):
		self.htmlwriter.htmlparagraph(text)
	def footer(self):
		self.htmlwriter.htmlfooter()

if __name__ == '__main__':
    textPage = Page('test', textRender())
    textPage.ren()

    htmlPage = Page('test1', htmlRender(htmlWriter()))
    htmlPage.ren()