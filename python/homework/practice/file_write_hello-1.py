f = open('test.txt', 'r')

while True:
  line = f.readline()
  if not line:
    break
  print(line) # 한 줄당 띄어쓰기
#   print(line.strip()) # 띄어쓰기(X)

f.close()
