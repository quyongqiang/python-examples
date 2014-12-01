import getopt
import sys
print sys.argv

def usage():
	print "get.py -i ip -p port"
try:  
  opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])  
except Exception, e:
  # print help information and exit: 
	print "error\n"
	sys.exit()
 
for name, value in opts:
	print name, value
for item in args:
     print item
