import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 입력 받기
A, B, C, X, Y = map(int, input().split())

# 양념과 후라이드 각각 개별로 구매하는 비용
individual_cost = A * X + B * Y

# 반반 치킨을 이용하여 양념과 후라이드를 구매하는 비용
half_half_cost = 2 * C * max(X, Y)

# 반반 치킨을 이용하여 더 적은 개수만큼 구매하는 비용
half_half_less_cost = 2 * C * min(X, Y) + A * max(X - min(X, Y), 0) + B * max(Y - min(X, Y), 0)

# 가장 저렴한 비용 선택
min_cost = min(individual_cost, half_half_cost, half_half_less_cost)

print(min_cost)
