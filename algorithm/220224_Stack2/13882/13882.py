import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


def permut(i, r):
    global min_sum
    if i == r:
        num_sum = 0
        for j in range(i):
            num_sum += arr[j][bit[j]]
            if num_sum > min_sum:
                return
        num_sum_2 = num_sum
        if min_sum > num_sum_2:
            min_sum = num_sum_2
        return
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            permut(i + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    bit = [0] * N
    min_sum = 100
    permut(0, N)

    print(f"#{tc} {min_sum}")