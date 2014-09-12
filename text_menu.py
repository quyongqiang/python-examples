#/usr/bin/env python
"menu program"

import sys
import time

menu = '''
menu:
    1: get summary of list.
    2: get average of list.
    x: exit the program.  '''
menu_dic = {1:'add', 2:'avg'}
def prompt():
    print menu

def add():
    sum = 0
    list1 = list(eval(raw_input("please input a list, at least two numbers:")))
#     print 'ok'
    for i in list1:
        sum += i
    print 'the sum of the list is:',sum

def avg():
    sum = 0
    avg = 0
    list1 = list(eval(raw_input("please input a list, at least two numbers:")))
#     print 'ok'
    for i in list1:
        sum += i
    avg = sum / float(len(list1))
    print 'the average of the list is:',avg



if __name__=='__main__':
    while True:
        prompt()
        cmd = raw_input('please input your choice:')
        try:
            cmd1 = int(cmd)
            sum_list = eval(menu_dic[cmd1])()
        except:
            if cmd == 'x':
                print 'bye'
                sys.exit()
            else:
                print 'input error'
                time.sleep(1)
