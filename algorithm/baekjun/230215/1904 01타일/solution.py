import sys
sys.stdin = open('input.txt', encoding='UTF-8')
from math import factorial
N = int(input())
num_1 = N
num_0 = 0
cnt = 0
num_sum = N
while True:
    if num_1 <= -1:
        break
    cnt += (factorial(num_sum) / (factorial(num_1) * factorial(num_0))) % 15746
    num_1 -= 2
    num_0 += 1
    num_sum = num_1 + num_0

print(f'{cnt:.0f}')

'''
메모리초과를 예상하고 코드를 돌려봤으나 그 이전에 시간초과가 되어버리는 코드이다.
'''