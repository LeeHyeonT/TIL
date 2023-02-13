import sys
sys.stdin = open('input.txt', encoding='UTF-8')

nA, nB = map(int, input().split())
num_dict = {}
A = input().split()
B = input().split()

for i in A:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1

for j in B:
    if j not in num_dict:
        num_dict[j] = 1
    else:
        num_dict[j] += 1

answer = 0
for k in num_dict:
    if num_dict[k] == 1:
        answer += 1
    else:
        continue

print(answer)

'''
set 을 활용하지 않는다면 dictionary 를 이용해서 문제를 풀 수 있음
원소 다 저장해놓고 갯수 1인 것들만 세어내면 반복을 최대 200,000 번 밖에 진행하지 않음
'''