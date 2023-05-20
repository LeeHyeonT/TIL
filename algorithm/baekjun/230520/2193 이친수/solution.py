import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
if n == 1 or n == 2:
    print(1)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    
    print(dp[n])

'''
오랜만에 풀어본 dp 문제
오랜만이라 감이 다 떨어져서 내가 푼 다른 문제를 참고 후 풀었다
그래도 한 번에 잘 풀려서 다행....
'''