# 문자열
s = 'Welcome to Python'
print(s.split())

d = '2023.10.20'
print(d.split('.'))

s1 = 'Hello, World!' # ' '(= 공백)까지 포함해서 분리됨..
print(s1.split(','))

s2 = 'Welcome, to, Python, and , bla, bla   '
print([s2.strip() for x in s2.split(',')])
