import getopt, sys

def usage():
    print "usage: python geto.py -h --help,-o --output, -v"

def pt_arg():
    print "test"
    print "sys.argv is: %s" % sys.argv
    print "sys.argv[1:] is: %s" % sys.argv[1:]
    print "sys.argv[:-1] is: %s" % sys.argv[:-1]
    print "sys.argv[:] is: %s" % sys.argv[:-1]

    #print  sys.argv

def main():
    #pt_arg()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvo:x:", ["help", "output="])
	print args[0]
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
#    pt_arg()
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
	    print 'you set -v'
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            #output = a
	    with open ('num', 'w') as n:
        	n.write(str(a))
        	n.write('\n')
	elif o in ("-x"):
	    print "you set -x %s" % a
        else:
            assert False, "unhandled option"
    # ...


if __name__ == "__main__":
    main()

