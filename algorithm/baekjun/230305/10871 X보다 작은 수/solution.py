import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, X = map(int, input().split())
num_array = list(map(int, input().split()))

for i in range(N):
    if num_array[i] < X:
        print(num_array[i], end=' ')

