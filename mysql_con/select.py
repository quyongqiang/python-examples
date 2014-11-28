# encoding: utf-8
#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",user="root",passwd = "123",db = "sampdb",port= 3308 )

cursor = db.cursor()

cursor.execute("show tables;")

data = cursor.fetch()

print " %s " % data

db.close()
