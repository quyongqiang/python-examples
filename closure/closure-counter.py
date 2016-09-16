#
# form: core python programing

def counter(start_at=0):
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	return incr



count = counter(2)
print count()
print count()
print count()


	In [1]: def counter(start=0):
	...:     count = [start]
	...:     def incr():
	...:         count[0] += 1
	...:         return count[0]
	...:     return incr
	...:
	In [2]: count = counter(5)

	In [3]: count
	Out[3]: <function __main__.incr>

	In [4]: count
	Out[4]: <function __main__.incr>

	In [5]: print count()
	6

	In [6]: print count()
	7
