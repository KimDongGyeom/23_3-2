# cipher(암호) <->decipher(해독하다)
# Encryption(암호화) <-> decryption(복호화)

import string

src_str = string.ascii_uppercase
dst_str = src_str[3:] + src_str[:3]

def cipher(a):
  idx = src_str.index(a)
  return dst_str[idx]

src = input('문장을 입력하시오(대소문자 구분 X):').upper()
print('암호화된 문자: ', end = '')

for ch in src:
  if ch in src_str: #== 알파벳이면
    print(cipher(ch), end='')
  else: # 알파벳이 아니면(= 그대로 리턴)
    print(ch, end='')
