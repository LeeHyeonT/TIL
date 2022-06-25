import sys
sys.stdin = open('input.txt', encoding='UTF-8')

from fractions import Fraction

N = int(input())
radius_lst = list(map(int, input().split()))
for i in range(1, len(radius_lst)):
    if radius_lst[0] % radius_lst[i] == 0:
        print(f'{radius_lst[0] // radius_lst[i]}/{int(1)}')
    else:
        print(Fraction(radius_lst[0] / radius_lst[i]))


# 출력 초과 가 나온다....
# 왜 그런지는 모르겠다....
