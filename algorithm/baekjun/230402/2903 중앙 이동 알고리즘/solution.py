import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
print((2**n+1)**2)