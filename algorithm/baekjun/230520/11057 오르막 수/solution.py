import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(n)]
for i in range(10):
    dp[0][i] = 1
for j in range(1,n):
    for k in range(10):
        if k == 0:
            dp[j][k] = dp[j-1][k]
        else:
            dp[j][k] = dp[j][k-1] + dp[j-1][k]

ans = sum(dp[n-1]) % 10007
print(ans)

'''
이중 list 로 dp를 꾸며야하는 것을 깨닫는다면 --> 규칙을 찾는다면 어렵지 않은 문제
'''