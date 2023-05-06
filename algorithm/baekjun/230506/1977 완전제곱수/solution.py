import sys
sys.stdin = open('input.txt', encoding='UTF-8')
import math

# 입력값 받기
m = int(input())
n = int(input())

# 완전제곱수 찾기
squares = []
for i in range(m, n+1):
    if int(math.sqrt(i))**2 == i:
        squares.append(i)

# 완전제곱수의 합과 최솟값 구하기
if squares:
    total = sum(squares)
    min_square = min(squares)
    print(total)
    print(min_square)
else:
    print("-1")
