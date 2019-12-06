class student:
	scl="Government"
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3
	def avg(self): #instance method
		return (self.m1+self.m2+self.m3)/3
	def get_m1(self): #Accessor method (get the value)
		return self.m1
	@classmethod
	def clsmet(cls):
		return cls.scl
	@staticmethod
	def sta():
		print("Hii welcome to all")
	def set_m1(self,va):  #Mutator method (can change the value)
		self.m1=va

s1=student(45,60,70)
s2=student(70,85,90)

print(s1.avg())
print(s2.avg())
print(s1.m1)
s1.set_m1(96)
print(s1.m1)
print(student.clsmet())
student.sta()
	
