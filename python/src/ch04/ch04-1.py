
def get_sum(start, end):
  sum = 0
  for i in range(start, end+1):
    sum += i
  return sum

sum = get_sum(1, 20);
print(sum);


