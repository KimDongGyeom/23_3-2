first_name = ['Kim', 'Park', 'Lee', 'Hong']

# 복제본을 복사하는 방법1
list = list(first_name)

# 복제본을 복사하는 방법2
a_list = first_name[:]

list[1] = 'Choi'

a_list[2] = 'Lee2'

print(id(first_name))
print(id(list))
print(id(a_list))

print(first_name)
print(list)
print(a_list)
