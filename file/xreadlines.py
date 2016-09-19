f = open('file.txt', 'r')

lines = f.xreadlines()

for line in lines:
	print line,

f.close
