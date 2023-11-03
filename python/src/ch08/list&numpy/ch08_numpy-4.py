import numpy as np

array_a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array_b = np.array(range(0, 10))
array_c = np.array(range(0, 10, 2))

print('실습 1 :', array_a)
print('실습 2 :', array_b)
print('실습 3 :', array_c)
print('실습 4 :')
print('shape: ', array_c.shape) # 투플의 형태이기 때문에, 괄호와 같이 나타남 (n,) n == 원소의 갯수
print('ndim: ', array_c.ndim) # n차원이라는 의미
print('dtype: ', array_c.dtype) # data type // 보통은 int32, int64의 형태로 메모리를 할당함!! 속도에도 유리(너무 잘게 나눌 경우, 효율이 무조건 좋지는 않음)
print('size: ', array_c.size) # 원소의 갯수
print('itemsize: ', array_c.itemsize) # a 객체 내부에 자료형이 차지하는 메모리 크기(byte)
