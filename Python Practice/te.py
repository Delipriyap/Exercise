import re
fp = open("manifest.xml","r");

while 1:

    line = fp.readline()

#    print line

    if(str(line).find('fetch') != -1):

        break

  

st=str(line)

print (st.partition('fetch="')[2]).split('"')[0]

 
