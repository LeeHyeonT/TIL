import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num_lst = []
for _ in range(N):
    num = int(input())
    num_lst.append(num)

num_lst.sort()
tmp = 2
res_lst = []
while True:
    if tmp >= num_lst[1]:
        break
    namuzi_lst = []
    for i in num_lst:
        namuzi = i % tmp
        namuzi_lst.append(namuzi)
    namuzi_lst.sort()
    if namuzi_lst[0] == namuzi_lst[-1]:
        res_lst.append(tmp)
    
    tmp += 1

for j in res_lst:
    print(j, end=' ')

# 다음에 다시 해보자!