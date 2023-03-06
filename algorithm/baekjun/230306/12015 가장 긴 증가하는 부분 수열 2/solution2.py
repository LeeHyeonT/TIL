import sys
sys.stdin = open('input.txt', encoding='UTF-8')

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
l = [a[0]]

for i in range(1, n):
    if a[i] > l[-1]:
        l.append(a[i])
        dp[i] = len(l) - 1
    else:
        idx = bisect_left(l, a[i])
        l[idx] = a[i]
        dp[i] = idx

# print(len(l))
seq = []
last_idx = len(l) - 1
for i in range(n - 1, -1, -1):
    if dp[i] == last_idx:
        seq.append(a[i])
        last_idx -= 1
seq.reverse
print(len(seq))

'''
가장 긴 증가하는 수열의 길이, 가장 긴 증가하는 수열 그 자체까지 구할 수 있는 코드
이게 궁극적인 이 문제의 정답...!
'''