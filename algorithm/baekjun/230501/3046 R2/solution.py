import sys
sys.stdin = open('input.txt', encoding='UTF-8')

r1, s = map(int, input().split())
print(s*2 - r1)