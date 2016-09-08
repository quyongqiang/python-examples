# by quyq

def fab(a, b, end):
	if a + b > end:
		print b
	else:
		print b
		fab(b, a + b, end)


print "1"
fab(1, 1, 50)