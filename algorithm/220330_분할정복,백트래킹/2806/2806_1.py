import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy

def queen(lst, array):
    global cnt
    array[lst[0]][lst[1]] = 1
    # print(f"전#{tc} i:{lst[0]} j:{lst[1]} array:{array}")
    for k in range(8):
        ii = lst[0]
        jj = lst[1]
        while True:
            ni = ii + di[k]
            nj = jj + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                break
            else:
                array[ni][nj] = -1
                ii = ni
                jj = nj
    # print(f"후#{tc} i:{lst[0]} j:{lst[1]} array:{array}")

    # 종료조건
    tmp1 = 0
    tmp2 = 0
    for end in array:
        if 0 not in end:
            tmp1 += 1
    if tmp1 == N:
        for end in range(N):
            tmp2 += sum(array[end])
        if tmp2 == N*(-N +2):
            cnt += 1
            return
        else:
            return


    for a in range(N):
        if array[lst[0]+1][a] == 0:
            array_copy = deepcopy(array)
            q_arr.append(array_copy)
            q_idx.append([lst[0]+1, a])


    for a in range(N):
        if array[lst[0] + 1][a] == 0:
            queen(q_idx.pop(-1), q_arr.pop(-1))



T = int(input())
# 대각선까지 여덟 방향 delta
di = [0,0,1,1,1,-1,-1,-1]
dj = [1,-1,0,1,-1,0,1,-1]
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        q_idx = [[0,i]]
        arr_copy = deepcopy(arr)
        q_arr = [arr_copy]
        queen(q_idx.pop(0), q_arr.pop(0))

    print(f"#{tc} {cnt}")
