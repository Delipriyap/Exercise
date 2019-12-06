class demo:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("am in __INIT__ method")
	def fun(self):
		print("am in function",self.name,self.age)

d=demo('priya',21)
d.fun()
