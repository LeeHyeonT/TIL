import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
storage = [0] * (101)
nums = list(map(int, input().split()))
reject = 0
for num in nums:
    if storage[num] == 0:
        storage[num] += 1
    else:
        reject += 1

print(reject)