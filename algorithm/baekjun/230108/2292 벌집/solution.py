import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
count = 1
n = 0
while True:
    if N == 1:
        break
    elif N >= 3*n*n - 3*n + 2 and N < 3*n*n + 3*n + 2:
        break
    n += 1
    count += 1

print(count)

'''
계차수열 문제인데 수학 다 까먹었네...이런
'''