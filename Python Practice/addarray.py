from array import *
a=array('i',[])
n=int(input("Enter the range:"))
for i in range(n):
	val=int(input("Enter the value:"))
	a.append(val)
print(a)
ser=int(input("Enter the search value:"))
'''k=0
for j in a:
	if j==ser:
		print(k)
		break
	k+=1'''
print(a.index(ser))


	
