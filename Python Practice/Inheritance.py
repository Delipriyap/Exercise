class A:
	def fun1(self):
		print("Hello")
	def fun2(self):
		print("Welcome")
class B(A):#Single level Inheritance
	def fun3(self):
		print("Function 3 is working")
	def fun4(self):
                print("Function 4 is working")
class C:
	def fun5(self):
		print("Thankyou")
class D(B,C):#Multiple Inheritance 
	def fun6(self):
		print("End")
a=A()
a.fun1()
a.fun2()
b=B()
b.fun1()
b.fun2()
b.fun3()
b.fun4()
c= C()
c.fun5()
d=D()
d.fun6()
d.fun5()
d.fun4()
d.fun3()
d.fun2()
d.fun1()
