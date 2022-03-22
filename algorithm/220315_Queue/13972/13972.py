import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')
from pprint import pprint
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    string = 0
    maze = []
    for _ in range(N):
        string = input()
        maze.append(list(map(int, str(string))))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
    print(start)
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    q = deque()
    visited = []
    q.append(start)
    visited.append(start)
    cnt = 0
    while q:
        [x, y] = q.popleft()
        visited.append([x, y])

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if (0 <= ni < N and 0 <= nj < N
                    and maze[ni][nj] != 1 and [ni, nj] not in visited):
                if maze[ni][nj] == 3:
                    cnt += 1
                    break
                else:
                    cnt += 1
                    q.append([ni, nj])

                    # if len(q) == 0:
                    #     cnt = 0
                    #     break

        print(q)

    print(f"#{tc} {cnt}")
