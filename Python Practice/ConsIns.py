class A:
	def __init__(self):
		print("Hii")
	def fun1(self):
		print("Hello")
class B(A):
	def __init__(self):
		super().__init__()
		print("Hello world")
	def fun2(self):
		print("welcome")
a=B()
