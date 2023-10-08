def get_square(a, b, c):
  a2 = a**2
  b2 = b**2
  c2 = c**2
  return a2, b2, c2

a, b, c = 1, 2, 3
a_sp, b_sp, c_sp = get_square(a, b, c)


print (a, '제곱: ', a_sp, ',', b, '제곱: ',  b_sp, ',', c , '제곱: ',  c_sp)
