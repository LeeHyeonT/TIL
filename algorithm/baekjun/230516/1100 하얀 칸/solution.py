import sys
sys.stdin = open('input.txt', encoding='UTF-8')

storage = []
for _ in range(8):
    array = list(map(str, input().split()))
    storage.append(array)

ans = 0
for i in range(len(storage)):
    for j in range(len(storage[i][0])):
        if i % 2 == 0:
            if j % 2 == 0 and storage[i][0][j] == 'F':
                ans += 1     
        else:
            if j % 2 == 1 and storage[i][0][j] == 'F':
                ans += 1
                
print(ans)