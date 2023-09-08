weight = float(input('weight input: '))
height = float(input('height input: '))

BIM = weight / (height * height)
# BIM = weight / height**2 # 같은 의미
print(BIM)
