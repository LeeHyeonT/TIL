import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a, b, c, d = map(str, input().split())
print(int(a+b) + int(c+d))