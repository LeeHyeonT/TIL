import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    dp = [0] * 10001
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[n])
    
'''
문제를 잘 읽자
0번째도 존재하므로 dp 갯수를 10,000 개가 아닌 10,001 개로 해야한다!
'''