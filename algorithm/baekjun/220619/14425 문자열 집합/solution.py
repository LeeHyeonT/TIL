import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())
word_dict = dict()
for i in range(N):
    word_dict[input()] = i

count = 0

for _ in range(M):
    if input() in word_dict:
        count += 1

print(count)

# 문제가 애매했음
'''
주어진 문자: AB
확인 문자열: CABD
일 때 이것도 맞는 것인지에 대해 문제 설명이 부족함...
'''
# 일단은 정확히 똑같은 경우에만 구하는 문제인 것으로!