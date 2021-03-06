# -*- coding: utf-8 -*-  

class HelloWorld(object):
	"""test local variablie, instance variable, class variable"""
	# class variable
	c_var = "class variable c_var"
	name = "name at class"
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
h2 = HelloWorld("ruby")
print h1.name
print HelloWorld.name

# 以下意思是调用实例变量c_var, 在实例变量c_var没有定义时，返回了类变量c_var
print h1.c_var


# 定义了实例变量c_var 
h1.c_var= "c_var changed instance var"
print h1.c_var	
print "##"

HelloWorld.c_var = "a"
print HelloWorld.c_var


h1.greet()

print ""
h1.test_name()

print ""
h1.pt_name()