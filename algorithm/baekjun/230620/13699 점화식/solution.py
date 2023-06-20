import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def func(n):
    global dp
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]
    
    return dp[n]

n = int(input())
ans = func(n)
print(ans)

'''
오랜만에 함수를 사용해보았다.
굳이 사용하지 않아도 풀 수 있지만 좀 더 깔끔한 느낌을 줄 수 있다.
'''