#
#有with语句就不再需要包含一个finally组来处理文件的关闭。

# 使用with就不再需要finally了
try:
  with open('its.txt', 'w') as data:
    print("It's...", file=data)
except IOError as err:
  print('File error: ' + str(err))


# 这是通常的try/except/finally模式
try:
  data=open('its.txt', 'w')
  print("It's...", file=data)
except IOError as err:
  print('File error: ' + str(err))
finally:
  if 'data' in locals():
    data.close
    
