import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n = int(input())
ans = 1001
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    if a > b:
        continue
    else:
        if b < ans:
            ans = b

if ans == 1001:
    print(-1)
else:
    print(ans)