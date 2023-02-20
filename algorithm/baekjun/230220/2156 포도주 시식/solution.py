import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
drink = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = drink[0]
for i in range(1, n):
        if i >= 3:
            dp[i] = max(dp[i-2] + drink[i], dp[i-1], dp[i-3] + drink[i-1] + drink[i])
        elif i == 1:
            dp[1] = drink[0] + drink[1]
        elif i == 2:
            dp[2] = max(dp[1], dp[0] + drink[2], drink[1] + drink[2])
            
print(max(dp))

'''
dp 조건을 분명 저렇게 작성한 기억이 있는데 (정확히는 맞는지 틀린지 돌려본 기억이 있는데) 왜 실제로 하지 않았을까...?
이 아이디어는 잘 떠올렸으니 내 스스로 맞춘 거라고 해도 되겠지...? 
다만 i==2 일 때 조건을 적게 설정하여 틀린 것은 엄연한 내 잘못이다.
'''