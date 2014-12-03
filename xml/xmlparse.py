def TestMiniDom():
  from xml.dom import minidom
  doc = minidom.parse("employees.xml")
  
  # get root element: <employees/>
  root = doc.documentElement
  
  # get all children elements: <employee/> <employee/>
  employees = root.getElementsByTagName("employee")
  
  for employee in employees:
    print("-------------------------------------------")
    # element name : employee
    print (employee.nodeName)
    # element xml content : <employee><name>windows</name><age>20</age></employee>
    # basically equal to toprettyxml function
    print (employee.toxml())
    
    nameNode = employee.getElementsByTagName("name")[0]
    print (nameNode.childNodes)
    print (nameNode.nodeName + ":" + nameNode.childNodes[0].nodeValue)
    ageNode = employee.getElementsByTagName("age")[0]
    print (ageNode.childNodes)
    print (ageNode.nodeName + ":" + ageNode.childNodes[0].nodeValue)
    
    print("-------------------------------------------")
    # children nodes :  \n is one text element
    # [
    # <DOM Text node "' \n    '">, 
    # <DOM Element: name at 0xc9e490>, 
    # <DOM Text node "'\n    '">, 
    # <DOM Element: age at 0xc9e4f0>, 
    # <DOM Text node "'\n  '">
    # ] 
    for n in employee.childNodes:
      print (n)

TestMiniDom()
