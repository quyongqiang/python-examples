#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# 5-5

num = 105
# res = list1[1,2]
# print res[-1]

list1 = [1, 5, 10, 25]
x = len(list1)
print x
list2 = []

def fun(num, x, l):
#     print num / x
    if x > 0:
        x = x - 1
    else:
        return
    res = num / l[x]
    num = num % l[x]
    print '%d * %d ' % (res, l[x])
    list2.append((res, l[x]))
    fun(num, x, l)
#    fun(num % x, list1.)

a = fun(num, x, list1)

# output the result use list format
print list2
