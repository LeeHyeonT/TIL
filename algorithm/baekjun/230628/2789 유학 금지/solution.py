import sys
sys.stdin = open('input.txt', encoding='UTF-8')

rule = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = input()
storage = []
for a in word:
    storage.append(a)

for b in range(len(storage)):
    if storage[b] in rule:
        storage[b] = ''

print(''.join(storage))

'''
이렇게도 풀 수 있다는 것을 보여주기위한 풀이
원래는 not in 써서 sting 형식 그대로 진행해도 되지만 list 에 하나하나 다 넣어놓고 진행
'''