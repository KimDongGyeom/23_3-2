import random
quotes = []
quotes.append('분노는 바보들의 가슴 속에서만 살아간다.')
quotes.append('소잃고 외양간 고친다.')
quotes.append('미운놈 떡하나 더 준다.')
quotes.append('시작이 반이다.')
quotes.append('고생끝에 낙이온다.')

print('#########################')
print('#        오늘의 명언       #')
print('#########################')

dailyQuote = random.choice(quotes)
print(dailyQuote)
