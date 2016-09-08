# coding:utf-8
# author: larry qu
# date: 2016-05

res=[1]

def fab(a, b, end):
	if a + b > end:
		res.append(b)
	else:
		res.append(b)
		fab(b, a + b, end)


fab(1, 1, 50)
print res


# 快点快点