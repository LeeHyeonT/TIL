import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num_array = list(map(int,input().split()))
dp = [0] * N

dp[0] = 1
for i in range(1, N):
    for j in range(i):
        # 증가하는 수열이 되려면 더 큰 값이 나와야하고 기준으로 삼고 있는 숫자의 최대 부분 수열보다 지금 돌고 있는 부분수열의 크기가 더 크다면
        if num_array[i] > num_array[j] and dp[i] < dp[j]:
            # 가장 긴 증가하는 부분 수열을 교체!
            dp[i] = dp[j]
            
    # 자기 자신을 이용하여 적어도 하나의 수열은 되기에 1을 더해줌
    dp[i] += 1

print(max(dp))
        
        
'''
(직접 푼 문제 x)
계속 고민하던 10, 20, 30, 1, 2, 3, 4, 5 이런 식으로 나왔을 때 어떻게 해아하는 가에 대한 문제를
if num_array[i] > num_array[j] and dp[i] < dp[j]
이 조건으로 해결해버렸다
원래 하려던 아이디어인 숫자를 저장하고 지지고 볶는 식으로 했다면 안 좋은 결과가 있었을 것...
'''