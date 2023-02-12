import sys
sys.stdin = open('input.txt', encoding='UTF-8')

words = list(map(str, input().split()))
print(len(words))