import functools
nums=[1,2,3,4,5,6,8,9,11,13,256,778]
evens=list(filter(lambda n:n%2==0 ,nums))
print(evens)
doubles=list(map(lambda n:n*2 ,evens))
print(doubles)
sum=reduce(lambda a,b:a+b, doubles)
print(sum)
