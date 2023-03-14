import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, m = map(int, input().split())
basket = []
for i in range(n+1):
    basket.append(i)
for _ in range(m):
    a, b = map(int, input().split())

    for j in range((b-a)//2 + 1):
        basket[a+j], basket[b-j] = basket[b-j], basket[a+j]
        
basket.pop(0)
for num in basket:
    print(num, end=' ')