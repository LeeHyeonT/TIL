# pruning 없는 코드... 시간초과가 난다
'''
해결 방법 : 2 x 2 짜리도 ㅗ 모양이랑 마찬가지로 따로 빼고
delta 할 때 위로 올라오는 방향 제외하고 진행하면 될듯 (아직 수정 x)
'''
def dfs(i,j):
    global cnt
    global tmp
    global maximum

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M and [ni,nj] not in visited:
            stack.append([ni,nj])
            visited.append([ni,nj])
            cnt += 1
            tmp += arr[ni][nj]

            if cnt == 4:
                if tmp > maximum:
                    maximum = tmp
                stack.pop()
                visited.pop()
                cnt -= 1
                tmp -= arr[ni][nj]
                continue
            else:
                dfs(ni,nj)
                stack.pop()
                visited.pop()
                cnt -= 1
                tmp -= arr[ni][nj]
                continue

def cross():
    global maximum

    for i in range(1,N-1):
        for j in range(1,M-1):
            tmp2 = arr[i][j]
            for k in range(4):
                tmp2 += arr[i+di[k]][j+dj[k]]
            for m in range(4):
                tmp3 = tmp2
                tmp3 -= arr[i+di[k]][j+dj[k]]
                if tmp3 > maximum:
                    maximum = tmp3

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 델타 탐색
di = [1,-1,0,0]
dj = [0,0,1,-1]

maximum = 0
for i in range(N):
    for j in range(M):
        stack = [[i,j]]
        visited = [[i,j]]
        cnt = 1
        tmp = arr[i][j]
        dfs(i,j)
        cross()

print(maximum)