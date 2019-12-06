def fact(n):
	if(n==0):
		return 1
	return n*fact(n-1)

c=int(input("Enter the value:"))
val=fact(c)
print(val)
