import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num_lst = list(map(int, input().split()))
num_dict = dict()
for i in range(N):
    num_dict[num_lst[i]] = i


M = int(input())
compare_lst = list(map(int, input().split()))

for j in range(M):
    if compare_lst[j] in num_dict:
        print('1', end=' ')
    else:
        print('0', end=' ')


# dictionary를 활용하여 시간복잡도를  O(1) 로 낮춰서 무난하게 성공!
# in 메서드도 list, tuple, set, dictionary 종류에 따라 시간복잡도 계산