import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a, i = map(int, input().split())
print(a*(i-1) + 1)