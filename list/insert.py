import re

# add_line is you need to added to your config file.
add_line = "add_header X-Frame-Options SAMEORIGIN;\n"

#pattern = re.compile('mime\.types;')
pattern = re.compile('nobody;')

with open('nginx.conf', 'r+') as f:
  f_list = f.readlines()
  index = 0

  for i in f_list:
    match = pattern.search(i)
    if match:
      print "matched index is:",index
      print "matched content line is:",i
      print "matched start pos is:",match.start()
      print "matched end pos is:",match.end()
      end = match.end()
      print "matched words is:%s" % (match.group())

      f_list.insert(index+1, add_line)
      f.seek(0, 0)
      f.writelines(f_list)

      print f.readlines()
      break
    else:
      index += 1
~
~
~
