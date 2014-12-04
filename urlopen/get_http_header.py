from urllib import urlopen    


doc = urlopen("http://www.baidu.com")    
print doc.info()    

print doc.info().getheader('Content-Type')
#print doc
