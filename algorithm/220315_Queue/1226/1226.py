import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

from collections import deque

for _ in range(1, 11):
    tc = int(input())
    string = 0
    maze = []
    res = 0
    for _ in range(16):
        string = int(input())
        maze.append(list(map(int, str(string))))


    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    q = deque()
    visited = []
    q.append([1,1])
    visited.append([1,1])
    res = 0
    while q:
        if res == 1:
            break
        [x,y] = q.popleft()
        visited.append([x,y])

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if maze[ni][nj] != 1 and [ni,nj] not in visited:
                if maze[ni][nj] == 3:
                    res = 1
                    break
                else:
                    q.append([ni, nj])

                    if len(q) == 0:
                        break

    print(f"#{tc} {res}")

# def bfs(i,j):
#     global res
#     q.append([i,j])
#     visited.append([i,j])
#     while q:
#         q.popleft()
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if maze[ni][nj] == 0 or maze[ni][nj] == 3:
#                 if maze[ni][nj] == 3:
#                     res = 1
#                     return res
#                 else:
#                     bfs(ni, nj)