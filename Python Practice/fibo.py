def fib(n):
	a=0
	b=1
	if n>0:
		if n==1:
			print(i)
		else:
			print(a)
			print(b)
			for i in range(2,n):
				c=a+b
				a=b
				b=c
				if c<100:
					print(c)
	else:
		print("Invalid Value")
c =int(input("Enter the value :"))
fib(c)
