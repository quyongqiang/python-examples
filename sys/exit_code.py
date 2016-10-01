import sys


def a():
	print 'in a()'
	return

def b():
	print "in b()"
	return 13

def c():
	print "in c()"
	sys.exit(13)

a()
b()
c()
