import sys
sys.stdin = open('input.txt', encoding='UTF-8')

dp = list([0] * 15 for _ in range(15))
for i in range(1, 15):
    dp[0][i] = i
for j in range(1, 15):
    for k in range(1,15):
        dp[j][k] = dp[j][k-1] + dp[j-1][k]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])
    

'''
1년 전에는 틀렸던 문제지만 이제는 맞춘다...!
dp의 기본 원리만 알고 있다면 손쉽게 풀 수 있는 문제! 반복은 얼마 안 해서 시간 초과는 나지 않는다
'''