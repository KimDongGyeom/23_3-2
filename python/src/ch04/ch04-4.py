# ppt 39Page 참고

pay = int(input('시급을 입력해주세요. : '))
time = int(input('근무 시간을 입력해주세요. : '))

def weeklyPay(rate, hour):
  total = 0
  if hour < 30:
    total = rate * hour
    return total
  else:
    hour -= 30
    total = (rate * 30) + (rate*1.5 * hour)
    return total
weeklyPay(pay, time)
print('주급은: ', weeklyPay(pay, time))
