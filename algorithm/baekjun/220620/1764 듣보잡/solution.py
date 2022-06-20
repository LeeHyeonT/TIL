from html.entities import name2codepoint
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())

name_dict = dict()
for i in range(N+M):
    a = input()
    if a not in name_dict:
        name_dict[a] = 1
    else:
        name_dict[a] += 1


twice_people = []
for j in name_dict:
    if name_dict[j] == 2:
        twice_people.append(j)

twice_people.sort()

print(len(twice_people))
for k in twice_people:
    print(k)

# dictionary is a god!
# 시간복잡도 많이 줄여주는 일등공신 dictionary!