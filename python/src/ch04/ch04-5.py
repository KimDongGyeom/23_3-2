# 과제, ppt 42참고

def MinMax(mylist, method = 'max'):
  minVal = 0
  maxVal = 100

  if method == 'max' :
    for val in mylist :
      if val > maxVal :
        maxVal = val
      return maxVal
  elif method == 'min' :
