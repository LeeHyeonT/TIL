import sys
sys.stdin = open('input.txt', encoding='UTF-8')
N = int(input())
num_arr = list(map(int, input().split()))

count = 0
for num in num_arr:
    divisor = []
    for i in range(1,1001):
        if num % i == 0:
            divisor.append(i)
    if len(divisor) == 2:
        count += 1

print(count)

# 시간 초과 나올 줄 알았는데 안 나오네...?