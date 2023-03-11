import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, m = map(int, input().split())

basket = [0] * n
for _ in range(m):
    start, end, num = map(int, input().split())
    for i in range(start - 1, end):
        basket[i] = num

for ball in basket:
    print(ball, end= ' ')