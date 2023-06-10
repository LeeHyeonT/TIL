import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

t = int(input())
dp = [0] * 68
dp[0] = dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 68):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

for _ in range(t):
    n = int(input())
    print(dp[n])
    
'''
숫자가 좀만 더 커진다면 데이터 초과가 될 수도 있다.
'''