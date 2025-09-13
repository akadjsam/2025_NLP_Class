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

# print(zeros)
# print(ones)
# print(identity)
# print(range_based_array)
# print(linspace_array)

# 3차원 배열을 생성
array = np.array(
    [
        [
            [3, 2, 1],
            [4, 5, 6]
        ],
        [
            [9, 2, 31],
            [4, 15, -6]
        ]
    ]
)
# print(array[1, 0, 2]) # 31 출력
# print(array.shape) # 배열의 형태를 알려줌
# print(array.ndim) # 배열의 차원을 알려줌
# print(array.size) # 배열의 크기
# print(array.dtype) # 원소의 타입 확인


array = np.arange(1, 6)
# print(array)
# print(array[0]) # 처음 값 인덱싱
# print(array[4], array[-1]) # 맨 끝 인덱싱
# print(array[1:4], array[1:-1])
# print(array[::2]) # 전체를 출력하되 2칸씩 띄운후에 출력

arr2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
# print(arr2d[0, 1]) # 앞에는 행, 뒤에는 열 출력. 따라서 0행1열이므로 2 출력
# print(arr2d[:,1]) # 전체 행, 1열이므로 2와 5 출력

np.random.seed(50) # 시드값을 줘서 출력이 항상 같음
x = np.random.random(5) # 0~1 사이의 실수값을 뽑음
print(x)
y = np.random.randint(1, 7, 5) # 1에서 6 사이의 정수 5개 출력 (7은 미포함)
print(y)
z = np.random.normal(50, 10, 5) # 평균, 표준편차, 표본갯수 -> 정규분포 만들기
print(z)

# q = np.arange(1,6) #1~5 사이, 6은 미포함
q = np.array(["가위","바위","보"])
choice = np.random.choice(q, 2)
print(choice)