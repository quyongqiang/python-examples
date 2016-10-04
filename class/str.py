class P():
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name

if __name__ == '__main__':
	p1 = P("lily")
	print str(p1)
