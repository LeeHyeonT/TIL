import sys
sys.stdin = open('input.txt', encoding='UTF-8')

'''
실패한 코드
이유: 바로 전에 놓은 Queen 만 비교하려고 했는데 그러면 안 된다.
예전에 놓은 Queen도 현재 Queen 을 놓을 때 영향을 줄 수 있기 때문!
'''

# def Backtracking(x, y, former_x, former_y):
#     global cnt
#     if x == N:
#         cnt += 1
#         return
#     for i in range(y):      # 가로 탐색
#         if i == 0 and x == 0: # (0,0) 위치 보정
#             chess_array[x][i] = -1
#             Backtracking(x+1, y, former_x, former_y)
#         elif i != former_y and (x+i != former_x + former_y or x+i != former_x + former_y +2):
#             chess_array[x][i] = -1
#             former_y = i
#             former_x = x
#             Backtracking(x+1, y, former_x, former_y)    #  세로 탐색 by backtracking
#             chess_array[x][i] = 0

# N = int(input())
# chess_array = list([0] * N for _ in range(N))
# cnt = 0
# Backtracking(0, 4, 0, 0)

# print(cnt)

'''
올바른 코드
abs 를 활용해서 대각선에 위치하는 지를 나타내었다
또한 Queen 이 어느 열에 위치하였는지를 array 를 통해 나타내었다
--> 계속 새로운 값을 지정하지 않아도 되어 시간 절약에 도움을 줌
'''
def Backtracking(queen, N, row):
    global cnt
    if row == N:
        cnt += 1
        return
    for i in range(N):
        queen[row] = i
        for j in range(row):
            if queen[row] == queen[j] or abs(queen[row]-queen[j]) == abs(row-j):
                break
        else:
            Backtracking(queen, N, row+1)

N = int(input())
queen = [0] * N
cnt = 0
Backtracking(queen, N, 0)
print(cnt)
    