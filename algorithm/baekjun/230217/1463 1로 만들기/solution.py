import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def min_operations(n):
    dp = [0] * (n+1)
    for i in range(2, n+1):
        dp[i] = 1 + dp[i-1]
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i//2])
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i//3])
    return dp[n]

N = int(input())
min_ops = min_operations(N)
print(min_ops)

'''
chatGPT 의 힘으로 풀어본 첫 문제....대단하다 chatGPT
그래도 개념을 살펴보자면 일단 기본적으로 
dp[i] = 1 + dp[i-1]
는 무조건 실행 가능한 횟수가 되는데 이것이랑
1 + dp[i//2]
1 + dp[i//3]
이것들이랑 더 작은 값을 비교하여 나타내면 되는 문제이다.
'''