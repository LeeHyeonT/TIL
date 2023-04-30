import sys
sys.stdin = open('input.txt', encoding='UTF-8')

nums = list(map(int, input().split()))
nums.sort()
print(*nums)