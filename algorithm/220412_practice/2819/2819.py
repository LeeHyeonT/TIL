import sys
sys.stdin = open('input.txt', 'r')

di = [0,0,1,-1]
dj = [1,-1,0,0]

def dfs(i,j,cnt,res):
    # 길이 7 됐으면 set 값에 넣고 함수 return
    if cnt == 6:
        num_set.add(res)
        return
    # delta 방향따라 움직이며 진행
    for m in range(4):
        ni = i + di[m]
        nj = j + dj[m]
        if 0<=ni<4 and 0<=nj<4:
            # 숫자를 string 형태로 받아올 것이므로 계속 숫자의 string 값 더해줌
            dfs(ni, nj, cnt+1, res + str(arr[ni][nj]))

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split()))for _ in range(4)]
    num_set = set()
    # 격자가 4x4 밖에 안 되므로 다 순회해도 괜찮다
    for i in range(4):
        for j in range(4):
            cnt = 0
            res = str(arr[i][j])
            dfs(i,j,cnt,res)

    print(f"#{tc} {len(num_set)}")