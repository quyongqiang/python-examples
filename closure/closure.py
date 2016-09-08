# coding: utf-8
# 闭包

def out():
	free_variable = 1
	print free_variable, "\n"
	def inner():
		free_variable += 1
		# print free_variable, "\n"
		return free_variable
	return inner


f = out()
f()