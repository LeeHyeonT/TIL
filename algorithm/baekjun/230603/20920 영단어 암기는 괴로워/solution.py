import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().rstrip().split())
words = []
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)

counter = Counter(words)
ans = list(set(words))
ans.sort(key=lambda x: (-counter[x], -len(x), x))

for word in ans:
    print(word)
    

'''
Counter 내장함수를 이용하여 효과적으로 빈도수를 계산할 수 있다.
'''