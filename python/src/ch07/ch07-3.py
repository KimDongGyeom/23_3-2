import string

src_str = string.ascii_uppercase
print(src_str)

dst_str = src_str[1:] + src_str[:1]
print(dst_str)

n = src_str.index('A')
print('A의 인텍스:', n)
print('src_str의 A 위치에 있는 dst_str의 문자 =', dst_str[n]) # B
