import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N_str = str(input())
N_lst = []
for i in N_str:
    N_lst.append(int(i))

N_lst.sort(reverse=True)
for j in N_lst:
    print(j, end='')


# 머릿속에 그린 그대로 하니 바로 맞은 문제!