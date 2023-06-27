import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def maximum_soldiers(n, soldiers):
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if soldiers[j] > soldiers[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return n - max(dp)

# 입력 받기
n = int(input())
soldiers = list(map(int, input().split()))

# 결과 출력
print(maximum_soldiers(n, soldiers))