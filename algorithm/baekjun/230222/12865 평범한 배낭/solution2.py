import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
WV = []
for _ in range(N):
    WV.append(list(map(int, input().rstrip().split())))

dp = [[0] * (K+1) for _ in range(N+1)] 
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= WV[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-WV[i-1][0]] + WV[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp)
print(dp[N][K])


# def knapsack(w, v, k):
#     n = len(w)
#     dp = [[0] * (k+1) for _ in range(n+1)]

#     for i in range(1, n+1):
#         for j in range(1, k+1):
#             if j >= w[i-1]:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
#             else:
#                 dp[i][j] = dp[i-1][j]

#     return dp

# n, k = map(int, input().split())
# w = []
# v = []
# for i in range(n):
#     wi, vi = map(int, input().split())
#     w.append(wi)
#     v.append(vi)

# # knapsack 함수 호출
# result = knapsack(w, v, k)

# # 결과 출력
# print(result)



'''
chatGPT 의 힘을 빌려 풀어보았다.
아래 코드가 chatGPT 의 코드이고 위의 코드가 내 코드이다.
가능한 무게를 가지고 array 를 만드는 생각을 했어야했는데 그 생각을 하지 못했다...
좀 더 수련해야겠다.
'''