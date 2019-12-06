from array import *

val= array('i',[12,3,4,5,7])
print(val) 
print(val.buffer_info())
#print(val.typecode)
val.reverse()
print(val[0])
for i in val:
	print(i)
new= array(val.typecode,(e*e for e in val))
for j in new:
	print(j)
