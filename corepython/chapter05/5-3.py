#/usr/bin/env python
# -*- coding: utf-8 -*-   
import sys

def num():
	try:
		score = raw_input("please input your score, score is a integer in 0~100:")
		if score == 'q':
			sys.exit()
		else:
			score = int(score)
		if score < 0 or score > 100:
			print "input error"
		else:
			return score
	except ValueError:
		print "please input your score, score is a integer in 0~100"

def pt(s):
	print 'your score is %s' % s


def result(score):
	if score >= 90 and score <= 100:
		pt('A')	
	elif score >= 80 and score <= 90:
		pt('B')	
	elif score >= 70 and score <= 80:
		pt('C')	
	elif score >= 60 and score <= 70:
		pt('D')	
	elif score < 60 and score >= 0:
		pt('F')	

while True:
	print("q to quit the program.")
	score = num()
	result(score)
	print	
