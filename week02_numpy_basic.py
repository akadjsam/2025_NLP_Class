# 2주차 : 넘파이와 판다스에 대해서 수업한 내용

import numpy as np

# list1 = [1, 2, 3.7, "4", 5]
list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)

# print(list1)
# 타입이 서로 다른 값이 np.array에 입력되면 크기가 가장 큰 타입으로 묵시적 형 변환이 됨.
# print(array1) #numpy는 파이썬의 list에 비해 속도가 빠름. 타입 검사를 하지 않기 때문. 따라서 AI 분야에서는 list는 사용하지 않는다.


array2 = np.array([[1,2,3],[4,5,6]])
# print(array2)

zeros = np.zeros((3,4)) # 3x4 행렬을 0으로 채움
ones = np.ones((2,3)) # 2x3 행렬을 1로 채움
identity = np.eye(3) # 단위행렬,항등행렬
range_based_array = np.arange(0,10,2) # 0부터 8까지 2씩 증가
linspace_array = np.linspace(0,100,5) # 0부터 100까지 5개의 구간으로 행렬 생성

print(zeros)
print(ones)
print(identity)
print(range_based_array)
print(linspace_array)