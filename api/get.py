from urllib2 import Request, urlopen

request = Request('http://private-80f7b-test8600.apiary-mock.com/questions')

response_body = urlopen(request).read()
print response_body
