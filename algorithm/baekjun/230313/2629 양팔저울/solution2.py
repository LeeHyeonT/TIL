import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
w = list(map(int, input().split()))
m = int(input())
beads = list(map(int, input().split()))

dp = [[False] * 40001 for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    for j in range(40001):
        if dp[i-1][j]:
            dp[i][j] = True
            dp[i][j+w[i-1]] = True
            dp[i][abs(j-w[i-1])] = True

for bead in beads:
    if dp[n][bead]:
        print('Y', end=' ')
    else:
        print('N', end=' ')