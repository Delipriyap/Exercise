import subprocess
from subprocess import*

import re

output=subprocess.Popen(["ifconfig"],stdout=PIPE)
file=output.stdout.read().decode('utf-8')
print(file)
var1 = re.search(r'\d+.\d+.\d+.\d+',file)
var2=re.search(r'\w+:\w+:\w+:\w+:\w+:\w+',file)
if var1:
    print(var1.group())
else:
    print("No pattern found")
if var2:
    print(var2.group())
else:
    print("no pattern found")



    
