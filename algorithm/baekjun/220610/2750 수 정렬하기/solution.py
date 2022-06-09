import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())

num_lst = []
for _ in range(N):
    num = int(input())
    num_lst.append(num)

for i in range(N-1):
    for j in range(N-i-1):
        if num_lst[j] > num_lst[j+1]:
            num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]

for k in range(len(num_lst)):
    print(num_lst[k])


# 문제에서 말하는 O(n2) 방법
# 효율성은 글쎄....?