import numpy as np

a = np.array(range(1,11)) + np.array(range(10, 101, 10))


print(a)
print()
print('shape: ', a.shape) # 투플의 형태이기 때문에, 괄호와 같이 나타남 (n,) n == 원소의 갯수
print('ndim: ', a.ndim) # n차원이라는 의미
print('dtype: ', a.dtype) # data type // 보통은 int32, int64의 형태로 메모리를 할당함!! 속도에도 유리(너무 잘게 나눌 경우, 효율이 무조건 좋지는 않음)
print('itemsize: ', a.itemsize) # a 객체 내부에 자료형이 차지하는 메모리 크기(byte)
print('size: ', a.size) # 원소의 갯수
