# coding: utf-8
import datetime
 
 

# fib1是存粹无意义的写法
def fib1(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib1(n - 1) + fib1(n - 2)
 
 
known = {0: 0, 1: 1}
 
 
def fib2(n):
  if n in known:
    return known[n]
 
  res = fib2(n - 1) + fib2(n - 2)
  known[n] = res
  return res
 
 
if __name__ == '__main__':
  n = 40
  print(datetime.datetime.now())
 # print('fib1(%d)=%d' % (n, fib1(n)))
  print(datetime.datetime.now())
  print('fib2(%d)=%d' % (n, fib2(n)))
  print(datetime.datetime.now())


 # 在n=10以内时，fib1和fab2运行时间都很短看不出差异，但当n=40时，就太明显了，fib1运行花了35秒，fab2运行只花费了0.00001秒。