import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, k = map(int, input().split())
storage = [[0] * 7 for _ in range(2)]
for _ in range(n):
    s, y = map(int, input().split())
    storage[s][y] += 1

ans = 0
for i in range(2):
    for j in range(7):
        if storage[i][j] == 0:
            continue
        else:
            if storage[i][j] % k:
                ans += storage[i][j] // k + 1
            else:
                ans += storage[i][j] // k

print(ans)