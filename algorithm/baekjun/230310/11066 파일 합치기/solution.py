import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def merge_files(file_sizes):
    n = len(file_sizes)
    # dp[i][j] : i부터 j까지의 파일을 합치는 최소 비용
    dp = [[0]*n for _ in range(n)]

    # 부분합 계산
    sums = [0]*(n+1)
    for i in range(1, n+1):
        sums[i] = sums[i-1] + file_sizes[i-1]

    # dp 계산
    for gap in range(1, n): # 얼만큼 띄우고 더해볼지 생각하는 값
        for i in range(n-gap): # i는 시작점
            j = i + gap # j는 종결점
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + sums[j+1] - sums[i]       
                dp[i][j] = min(dp[i][j], cost)
                
    return dp[0][n-1]

t = int(input())
for _ in range(t):
    k = int(input())
    file_sizes = list(map(int, input().split()))
    print(merge_files(file_sizes))
        