import sys
sys.stdin = open('input.txt')

for _ in range(10):
    arr = []
    Idx = int(input())
    for i in range(100):
        arr += [list(map(int, input().split()))]

    # 행, 열, 대각선, 역대각선 합 구하기
    DiaSum = 0
    DiaRevSum = 0
    RowMaxSum = 0
    ColMaxSum = 0
    # 행, 열들 합 비교 후 각각의 최댓값 산출
    # 대각선 합까지 구함, for 문 밖에서 나온 4개의 값 비교 예정
    for j in range(100):
        RowSum = 0
        ColSum = 0
        for k in range(100):
            RowSum += arr[j][k]
            ColSum += arr[k][j]
        if RowSum >= RowMaxSum:
            RowMaxSum = RowSum
        if ColSum >= ColMaxSum:
            ColMaxSum = ColSum
        DiaSum += arr[j][j]
        DiaRevSum += arr[j][99-j]
    # 나온 4개의 값들 중 최댓값 찾기
    SumArray = [RowMaxSum, ColMaxSum, DiaSum, DiaRevSum]
    MaxSum = max(SumArray)

    print(f"#{Idx} {MaxSum}")