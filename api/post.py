from urllib2 import Request, urlopen

values = """
  {
    "question": "Favourite programming language?",
    "choices": [
      "Swift",
      "Python",
      "Objective-C",
      "Ruby"
    ]
  }
"""

headers = {
  'Content-Type': 'application/json'
}
request = Request('http://private-80f7b-test8600.apiary-mock.com/questions', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body