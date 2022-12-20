import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())

array_A = list(list(map(int, input().split())) for _ in range(N))
array_B = list(list(map(int, input().split())) for _ in range(N))

array_result = []
for i in range(N):
    hang = []
    for j in range(M):
        hang.append(array_A[i][j] + array_B[i][j])
    array_result.append(hang)

for m in range(N):
    for n in range(M):
        print(array_result[m][n], end=' ')
    print('')