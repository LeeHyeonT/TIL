import sys
sys.stdin = open('input.txt', encoding='UTF-8')
from itertools import combinations

N, goal = map(int, input().split())
num_lst = list(map(int, input().split()))

comb_3 = list(combinations(num_lst, 3))

res = 0
for i in range(len(comb_3)):
    if sum(comb_3[i]) <= goal and res < sum(comb_3[i]):
        res = sum(comb_3[i])

print(res) 