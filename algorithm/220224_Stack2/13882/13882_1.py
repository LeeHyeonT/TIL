# 되지만 메모리 초과.... 그럼 안 되는 거지 뭐

import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')


def permut(i, r):
    if i == r:
        permutation.append(bit[:])
        return
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            permut(i + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    # 순열 이용해서 가짓수 뽑아올 예정
    bit = [0] * N
    permutation = []
    permut(0, N)
    print(permutation)

    # 순열 이용해서 합의 최솟값 구하기
    min_sum = 100
    for i in range(len(permutation)):
        num_sum = 0
        for j in range(len(permutation[i])):
            num_sum += arr[j][permutation[i][j]]
        if min_sum > num_sum:
            min_sum = num_sum

    print(f"#{tc} {min_sum}")