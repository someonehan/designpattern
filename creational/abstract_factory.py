# -*- coding:utf-8 -*-  
#!/usr/bin/python

# 定义：创建一组相关联或者相互依赖的对象提供一个接口，并且无需指定他们的具体类
class DiagramFactory:
	@classmethod
	def make_diagram(cls, width, height):
		return cls.Diagram(width, height)

	@classmethod
	def make_rectangle(cls,width, height, fill='white'):
		return cls.Rectangle(width, height, fill)

	@classmethod
	def make_text(cls, x, y, text, fontsize=21):
		return cls.Text(x, y, text, fontsize)

	class Diagram:
		def __init__(self, width, height):
			print('Diagram Diagram created!')

	class Rectangle:
		def __init__(self, width, height, fill):
			print('Diagram Rectangle created')

	class Text:
		def  __init__(self,x, y, text, fontsize):
			print('Diagram Text created')

# SvgDiagramFactory 只需要继承DiagramFactory,而不需要在去实现那几个make方法了
# 由于svgDiagramFactory没有实现这个方法所以会执行基类的make方法，而在执行的时候cls参数就是svgDiagramFactory参数
# 这样以来基类就能够创建出svgDiagramFacrtory需要的make的对象从而能够返回了。
class SvgDiagramFactory(DiagramFactory):
	def __init__(self):
		pass

	class Diagram:
		def __init__(self, width, height):
			print('Svg Diagram created')
	class Rectangle:
		def __init__(self, width, height, fill):
			print('Svg Rectangle created')
	class Text:
		def __init__(self, x, y, text, fontsize):
			print('Svg text created')

if __name__ == '__main__':
	DiagramFactory.make_diagram(100, 100)

	SvgDiagramFactory.make_diagram(100, 100)