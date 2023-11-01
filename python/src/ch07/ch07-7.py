text = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPINTAL. NO EXAMS IN COVID!!!"
count = 0

l_text = text.lower()
print(l_text)
print('느낌표 갯수:', l_text.count('!'))

def a(ch):
  if ch.isupper:
    count += 1
  return count
