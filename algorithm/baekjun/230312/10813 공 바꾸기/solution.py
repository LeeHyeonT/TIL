import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, m = map(int, input().split())
basket = []
for i in range(n):
    basket.append(i+1)

for _ in range(m):
    a,b = map(int, input().split())
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

for num in basket:
    print(num, end=' ')