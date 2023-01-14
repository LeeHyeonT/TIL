import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num = input()
num_sum = 0
for n in num:
    num_sum += int(n)
print(num_sum)