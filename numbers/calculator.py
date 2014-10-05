#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# core python programing, 5-6


a = raw_input('please input your expression:')
l = a.split()



N1 = float(l[0])
N2 = float(l[2])

c = l[1]



def cal(c, N1, N2):
    if c == '*':
        print N1 * N2
    if c == '/':
        print  N1 / N2
    if c == '+':
        print N1 + N2
    if c == '-':
        print N1 - N2
    

cal(c, N1, N2)

