
# sample 1 
arr = [1, 2, 3]

def plus2(i):
	return i + 2

for i in map(plus2, arr):
	print i

print
print "########################"
print

# sample 2.

for i in map((lambda x: x+2), [1, 2, 3]):
	print i
