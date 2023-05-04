import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
storage = []
for _ in range(n):
    command = input()
    storage.append(command)

l = len(storage[0])
ans = ''
for i in range(l):
    for j in range(n-1):
        if storage[j][i] != storage[j+1][i]:
            ans += '?'
            break
        else:
            continue
    else:
        ans += storage[0][i]

print(ans)

'''
for-else 문을 잘 활용하면 쉬운 문제
'''