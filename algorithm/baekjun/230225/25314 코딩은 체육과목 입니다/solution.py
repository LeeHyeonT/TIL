import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
n = N // 4
for _ in range(n):
    print('long', end=' ')
print('int')