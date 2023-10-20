s = '    Hello, World!    '

print(s.strip())
print(s.lstrip())
print(s.rstrip())

print()

s1 = '#####this is an example#####'
print(s1)
print(s1.lstrip('#'))
print(s1.rstrip('#'))
print(s1.strip('#').capitalize())

print()

url = 'www.booksr.co.kr'
print(url.find('.kr')) # 시작 index
print(url.find('x')) # 없는 경우 -1을 return
print(url.count('.')) # .이 몇개인지

print(ord(max(url))) # s문자열 내 가장 유니코드 값이 가장 큰 값의 유니코드 값을 반환
print(ord(min(url))) # s문자열 내 가장 유니코드 값이 가장 작은 값의 유니코드 값을 반환
print('chr(119):', chr(119),'/' , 'chr(46):', chr(46))
