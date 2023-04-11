import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n = int(input())
arrays = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    arrays.append([a,b])
arrays.sort(key=lambda x: (x[1], x[0]))
for array in arrays:
    print(*array)


'''
lambda 사용법 잘 알기
'''