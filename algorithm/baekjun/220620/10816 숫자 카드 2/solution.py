import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num_lst = list(map(int, input().split()))

M = int(input())
check_num = list(map(int, input().split()))
check_dict = dict()

for i in check_num:
    check_dict[i] = 0

for j in num_lst:
    if j in check_dict:
        check_dict[j] += 1

for k in check_num:
    print(check_dict[k], end=' ')


# dictionary good!!!