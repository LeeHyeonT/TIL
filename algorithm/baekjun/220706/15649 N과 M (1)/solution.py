import sys
sys.stdin = open('input.txt', encoding='UTF-8')

from itertools import permutations
N, M = map(int, input().split())
n_lst = []
for i in range(1, N+1):
    n_lst.append(i)
permu = permutations(n_lst,M)

for j in permu:
    for k in j:
        print(k, end=' ')
    print('')

# itertools permutaion 만 안다면 쉽게 풀 수 있는 문제!
# 하지만 permutaion하는 로직은 알고 가야한다!