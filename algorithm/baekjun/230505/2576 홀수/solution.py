import sys
sys.stdin = open('input.txt', encoding='UTF-8')

storage = []
for _ in range(7):
    num = int(input())
    if num % 2 == 0:
        continue
    else:
        storage.append(num)
if len(storage) == 0:
    print(-1)
else:
    storage.sort()
    print(sum(storage))
    print(storage[0])