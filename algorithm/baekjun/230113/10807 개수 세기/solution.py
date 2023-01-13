import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_dict = {}
for num in num_list:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

V = int(input())
if V in num_dict:
    print(num_dict[V])
else:
    print(0)