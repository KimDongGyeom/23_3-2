import matplotlib.pyplot as plt

books = [3, 4, 3, 3, 0, 6, 0, 2]

# 6개의 bin(쓰레기 통을 이용하여 books 안에 저장된 자료의 히스토그램 그리기
plt.hist(books, bins = len(books))
# plt.hist(books, bins = 5) # bins는 2번째 인자로 무조건 와야하며, 최적의 bins는 무엇인지 고민을 해봐야함!!

# 책
plt.xlabel('books')
# 빈도 수
plt.ylabel('frequency')

plt.show()
