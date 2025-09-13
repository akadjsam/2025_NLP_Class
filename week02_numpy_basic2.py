import numpy as np

a = np.arange(1, 6)
mask = a > 2
# print(a[mask])
# print(a[a > 2])

result = np.where(a > 3, a, 0) # a에 있는 값들 중 3보다 큰 값들은 그대로 출력하고, 3보다 작거나 같으면 0으로 채우기
result = np.where(a > 3, a, a**2) # a에 있는 값들 중 3보다 큰 값들은 그대로 출력하고, 3보다 작거나 같으면 제곱으로 채우기
# print(result)

o = np.arange(1,13)
r = o.reshape(2, 2, 3) # 1차원 행렬을 3차원으로 변환, 2개의 매트릭스(2×3)를 가진 3차원 배열
r = o.reshape(4,3) # 4행 3열
# print(r)

f = r.flatten()
# print(f)

# 수학관련
m = np.array([4, 25, 9, 16])
# print(np.sqrt(m)) # 각각 원소에 대하여 연산 수행. broadcast
# print(np.exp(m)) # 지수값 e
# print(np.log(m)) # log함수
# print(np.log10(m)) # log10

n = np.array([0, np.pi/2, np.pi])
# print(np.sin(m))
# print(np.cos(m))
# print(np.tan(m))

r = m.reshape(2, 2)
# print(r)
# print(np.transpose(r)) # 전치행렬
# print(r.T)

