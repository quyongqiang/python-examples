class HelloWorld(object):
	"""test local variablie, instance variable, class variable"""
	# class variable
	name = 1
	def __init__(self, name):
		super(HelloWorld, self).__init__()
		self.name = name
		

	def greet(self):
		print self.name

	def test_name(self):
		# local variable
		name = "test_name function local var"
		# instance variable
		self.name = "lucy"
		print name
		print self.name
		print HelloWorld.name


	def pt_name(self):
		name = "pt_name function local var"
		print name
		print self.name
		print HelloWorld.name
h1 = HelloWorld("lily")
h1.greet()

print ""
h1.test_name()

print ""
h1.pt_name()