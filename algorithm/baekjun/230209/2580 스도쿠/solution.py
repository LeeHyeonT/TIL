import sys


# x 세로줄의 n이 있는지 확인
def checkRow(x, n):
    for i in range(9):
        if n == graph[x][i]:
            return False
    return True


# y 가로줄의 n이 있는지 확인
def checkCol(y, n):
    for i in range(9):
        if n == graph[i][y]:
            return False
    return True


# x, y 좌표가 포함되어 있는 3x3 크기의 사각형의 n이 있는지 확인
def checkRect(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True


# dfs + 백트래킹
def solution(n):
    # 스도쿠의 빈 칸을 채웠다면
    if n == len(blank):
        for _ in range(9):
            print(*graph[_])
        exit(0)

    # 반복문을 통해 빈칸에 1부터 9까지 넣어본다.
    for i in range(1, 10):
        x = blank[n][0] # 빈칸의 x좌표
        y = blank[n][1] # 빈칸의 y좌표

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            solution(n + 1)
            graph[x][y] = 0


graph = []
blank = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])

solution(0)


'''
*** 위의 코드는 제가 작성한 것이 아닙니다.
일단 아이디어 자체는 똑같지만 생각하는 방식이 달랐음
나는 바로 가로, 세로, 정사각형에 없는 것을 파악하려고 했는데 이렇게 하면 쉬운 스도쿠는 풀릴 질 몰라도 어려운 건 매우 많은 backtracking 을 실시하게되어 결국 시간초과가 날 수 밖에 없었음
따라서 빈칸의 위치를 파악 후 그것들만 반복문을 통해 돌며 가로, 세로, 정사각형에 들어갈 수 있는지 판단하는 작업을 거침
그러니 문제 해결!
(ps: 정사각형 표현할 때 x//3, y//3 으로 하는 아이디어는 바로 생각해야하는건데 잘 나지 않았음....) 
'''