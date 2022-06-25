import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
radius_lst = list(map(int, input().split()))

for i in range(1, len(radius_lst)):
    if radius_lst[0] > radius_lst[i]:
        tmp_big = radius_lst[0]
        tmp_small = radius_lst[i]
    else:
        tmp_big = radius_lst[i]
        tmp_small = radius_lst[0]
    GCD = 0
    while True:
        if GCD != 0:
            break

        if radius_lst[0] % tmp_small == 0 and radius_lst[i] % tmp_small == 0:
            GCD = tmp_small
        tmp_small -= 1
    print(f'{(radius_lst[0] // GCD)}/{(radius_lst[i] // GCD)}' )

# 시간복잡도 O(n^2) 라 걱정했는데 숫자 범위가 크지 않아서 가능한 것 같다!
