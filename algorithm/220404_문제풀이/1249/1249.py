import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def BFS(si,sj,fi,fj):
    global ans
    q = deque()
    visited = [[1000] * N for _ in range(N)]
    q.append((si,sj))
    visited[si][sj] = 0

    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + arr[ni][nj]

    ans = visited[fi][fj]


di = [1,-1,0,0]
dj = [0,0,1,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    BFS(0,0,N-1,N-1)

    print(f"#{tc} {ans}")