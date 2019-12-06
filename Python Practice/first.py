import re

filepath='Downloads/manifest.xml' 
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		line = fp.readline()
		cnt += 1
		val = re.match("fetch",line)
		print(re.search("fetch",line))

fp.close()



