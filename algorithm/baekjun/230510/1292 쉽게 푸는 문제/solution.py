import sys
sys.stdin = open('input.txt', encoding='UTF-8')

storage = [0]
key = 1
while True:
    if len(storage) >= 1001:
        break
    for _ in range(key):
        storage.append(key)
    key += 1
    
a, b = map(int, input().split())
print(sum(storage[a:b+1]))