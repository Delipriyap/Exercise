import re
n=input("enter the emailid:")  
var=re.search(r'(\w){1,20}\@(\w){5,10}\.(\w){2,3}',n)
if var:
    print(var.group())
else:
    print("please enter valid mailid:")
#^[A-Z0-9][A-Z0-9._%+-]{0,63}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$.
