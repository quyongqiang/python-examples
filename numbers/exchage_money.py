#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# core python programing , 5-5
"calculate how 105 cents can be made up"

num = 105
# res = list1[1,2]
# print res[-1]


# dollor have 1, 5, 10, 25 cents
list1 = [1, 5, 10, 25]
x = len(list1)
print x


def fun(num, x, l):
#     print num / x
    if x > 0:
        x = x - 1
    else:
        return
    res = num / l[x]
    num = num % l[x]
    print '%d * %d ' % (res, l[x])
    fun(num, x, l)
#    fun(num % x, list1.)

a = fun(num, x, list1)

