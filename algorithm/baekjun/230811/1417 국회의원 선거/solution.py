import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
n = int(input().rstrip())
me = int(input().rstrip())
storage = []
for _ in range(n-1):
    storage.append(int(input().rstrip()))
storage.sort(reverse=True)

cnt = 0
for i in range(len(storage)):
    if me >= storage[i]:
        break
    else:
        while True:
            if me >= storage[i]:
                break
            me += 1
            storage[i] -= 1
            cnt += 1

if me in storage:
    cnt += 1
    print(cnt)
else:
    print(cnt)
