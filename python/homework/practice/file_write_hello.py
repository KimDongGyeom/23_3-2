'''
f = open('hello.txt', 'w') # 파일명, write(= 쓰기)
f.write('Hello World!')
f.close()

f = open('hello.txt', 'r') # 파일명, write(= 쓰기)
s = f.read()
print(s)
f.close()
'''

f = open('test.txt', 'w')

f.write('===write test===\n')

lines1 = ['write\n', 'list\n', 'lines\n']
f.writelines(lines1)

lines2 = ['write\n', 'tuple\n', 'lines\n']
f.writelines(lines2)

f.close()
