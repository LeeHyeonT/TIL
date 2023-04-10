import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a, b, c = map(int, input().split())
print(a+b+c)