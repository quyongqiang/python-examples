import getopt
import sys
print sys.argv

def usage():
	print "get.py -i ip -p port"

try:
	options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])
#except getopt.GetoptError:
except Exception, e:
	#print e
	sys.exit()

print 'sys.argv is:',sys.argv[:],'\n'
#print 'sys.argc is:',sys.argc,'\n'
print "args[0] is:\n", args[0]
print "args[1] is:\n", args[0]
print "args[2] is:\n", args[0]

for name,value in options:
	if name in ("-h","--help"):
		usage()
	if name in ("-i","--ip"):
		print 'ip is----',value
	if name in ("-p","--port"):
		print 'port is----',value
