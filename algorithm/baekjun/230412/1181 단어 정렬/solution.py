import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n = int(input().rstrip())
storage = set()
for _ in range(n):
    word = input().rstrip()
    storage.add(word)
storage_list = list(storage)
storage_list.sort(key=lambda y: y)
storage_list.sort(key=lambda x: len(x))

for w in storage_list:
    print(w)
    
'''
input 20,000 개 정도라도 readline 은 써 주는것이 속도 향상에 크나큰 도움이 된다!
'''