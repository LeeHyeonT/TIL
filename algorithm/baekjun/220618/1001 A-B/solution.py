import sys
sys.stdin = open('input.txt', encoding='UTF-8')

num_lst = list(map(int, input().split()))

print(num_lst[0] - num_lst[1])