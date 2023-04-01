import sys
sys.stdin = open('input.txt', encoding='UTF-8')


array = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if array[i][j] == 1:
                continue
            else:
                array[i][j] = 1
    
ans = 0
for m in array:
    for n in m:
        if n == 0:
            continue
        else:
            ans += n

print(ans)