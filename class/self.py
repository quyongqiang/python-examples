class Stu(object):
	"""docstring for Stu"""
	def __init__(self, age):
		self.age = age
	
	def growup(self):
		self.age += 1

s1 = Stu(1)
s1.growup()
print s1.age