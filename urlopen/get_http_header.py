from urllib import urlopen    


doc = urlopen("http://www.baidu.com")    
print doc.info()    


print ("###")
print doc.info().getheader('Content-Type')
#print doc



h_163 = urlopen("http://www.163.com")    
print h_163.info() 