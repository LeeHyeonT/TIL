import sys
sys.stdin = open('input.txt', encoding='UTF_8')
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

answer_array = [([0] * K) for _ in range(N)]
A_y = 0
B_x = 0
for i in range(N):
    for j in range(K):
        A_y = 0
        B_x = 0
        while True:
            if A_y == M:
                break
            answer_array[i][j] += A[i][A_y] * B[B_x][j] 
            A_y += 1
            B_x += 1

for answer in answer_array:
    for number in answer:
        print(number, end=' ')
    print('')

'''
단순 행렬 곱셈 코딩으로 나타내는 문제지만
헷갈릴 만한 요소가 많다
A*B 인 경우 A의 행이 고정인지 B의 행이 고정인지, 또는 A의 열이 고정인지 B의 열이 고정인지
잘 판단해야 한다.
또한 반복문을 돌리면서 어떠한 값을 계속 초기화시켜줘야 할 것인지에 대해서도 고민이 필요하다.
'''