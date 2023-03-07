import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

# def get_min_cost(n, roads, prices):
#     min_cost = 0
#     min_price = prices[0]
    
#     for i in range(n-1):
#         if prices[i] < min_price:
#             min_price = prices[i]
#         min_cost += min_price * roads[i]
        
#     return min_cost

# # Example Usage
# n = 4
# roads = [2, 3, 1]
# prices = [5, 2, 4, 1]
# min_cost = get_min_cost(n, roads, prices)
# print(min_cost)  # Output: 18


n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

dp = [0] * n
min_price = prices[0]
distance = 0

for i in range(n-1):
    if prices[i] < min_price:
        min_price = prices[i]
    dp[i+1] = dp[i] + (min_price * distances[i])


print(dp[n-1])    