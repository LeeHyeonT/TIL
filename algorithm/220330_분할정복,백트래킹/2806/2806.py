import sys
sys.stdin = open('input.txt', 'r')

# 일단 이런 방식으론 접근 실패
def queen(i, j, array):
    for k in range(4):
        ii = i
        jj = j
        while True:
            ni = ii + di[k]
            nj = jj + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                break
            else:
                array[ni][nj] = -1
                ii = ni
                jj = nj
    if j >= 1:
        array[i][j-1] = -1

    # pruning 및 종료조건
    for prun in range(N):
        if arr[prun] not in 0:
            return

    while i+1 < N:
        if sum(array[i+1]) >= -N +2:
            for m in range(N):
                if arr[i+1][m] == 0:
                    array_copy = array[:]
                    queen(i,m,array_copy)
        elif sum(array[i+1]) == -N +1:
            for n in range(N):
                if arr[i+1][n] == 0:
                    queen(i+1, n, )


T = int(input())
# 남서, 남, 남동, 동쪽 방향 delta
di = [1,1,1,0]
dj = [-1,0,1,1]
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 배열 전체 순회할 것
    arr_copy = arr[:]
    for i in range(N):
        for j in range(N):
            if arr_copy[i][j] == 0:
                arr_copy[i][j] = 1
                queen(i, j, arr_copy)

