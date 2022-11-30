import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())
arrays_1 = []
for _ in range(N):
    arrays_1.append(list(map(int, input().split())))

M, K = map(int, input().split())
arrays_2 = []
for _ in range(M):
    arrays_2.append(list(map(int, input().split())))

print(arrays_1, arrays_2)

# N * K 행렬 생성
array_result = []
for _ in range(N):
    array_result.append(([[0, 0, 0] for _ in range(K)]))

# 계산 시작

x = 0
y = 0
while True:
    if y == K:
        break
    for array in arrays_1:
        for j in range(len(array)):
            array_result[x][y] = arrays_1[x][j] * arrays_2[j][y]
    y += 1
print(array_result)
