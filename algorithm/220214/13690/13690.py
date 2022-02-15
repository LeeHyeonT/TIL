import sys
sys.stdin = open('input.txt')
# 횟수 입력
T = int(input())
# 횟수만큼 수행
for num in range(T):
    # 문제에서는 5 고정이지만 다른 값도 들어갈 수 있도록
    col_row = int(input())
    arr = []
    # 행렬 생성
    for _ in range(col_row):
        arr += [list(map(int, input().split()))]
    # 델타: 우 하 좌 상 순으로 작용
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    abs_sum = 0
    for i in range(col_row):
        for j in range(col_row):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 조건에 맞는 경우에만 계산
                # abs 안 쓰려면 각각 값들 빼서 음수인 경우 - 붙여주는 식으로 가능
                if 0 <= ni < col_row and 0 <= nj < col_row:
                    abs_sum += abs(arr[i][j]-arr[ni][nj])
    print(f"#{num+1} {abs_sum}")
