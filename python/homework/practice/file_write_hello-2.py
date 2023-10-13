file_name = input('file명을 입력해주세요(.txt는 생략): ')

def process(w):
  output = ''
  for ch in w:
    if ch.isalpha():
      output += ch


f = open(file_name + '.txt', 'r')

while True:
  line = f.readline()
  if not line:
    break
#   print(line) # 한 줄당 띄어쓰기
  print(line.strip()) # 띄어쓰기(X)
  r_line = line.strip()

f.close()
