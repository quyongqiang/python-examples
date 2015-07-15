#!/usr/bin/python
# version: python 27
# Purpose: add your personal httpd header in GET request, "Test": "MyTestheader"
#         you can print the header infomation in nginx log, use:
#             # nginx.conf
#             log_format main1 '$remote_addr - "$http_test" ';
#             access_log  logs/access.log  main1;


import httplib, urllib
params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "Test": "MyTestheader"}

#conn = httplib.HTTPConnection("bugs.python.org")

conn = httplib.HTTPConnection("192.168.0.31")

#conn.request("POST", "", params, headers)

conn.request("GET", "", params, headers)

response = conn.getresponse()
print response.status, response.reason

data = response.read()
print data
conn.close()

