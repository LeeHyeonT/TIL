import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 기존에 완화된 조건 속에서 dynamic programming 으로 푼 풀이
# 이 문제에서는 시간 초과
'''
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

# 이분 탐색을 활용한 풀이
n = int(input())
a = list(map(int, input().split()))

# L = [a[0]]

# for i in range(1, n):
#     if a[i] > L[-1]:
#         L.append(a[i])
#     else:
#         left, right = 0, len(L) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if L[mid] >= a[i]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         L[right + 1] = a[i]
#     print(L)
# print(len(L))

'''
포인트는 마지막에 나오는 L 이 우리가 원하는 모양이 아닐지라도 어쨌든 길이의 크기만 구하면 되는 문제이기에 크게 상관없다는 점이다.
다만 나중에 실제 수열 그 자체를 구하는 문제에서는 이런 방식으로 풀 수는 없다.
'''
