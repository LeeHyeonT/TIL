import sys
sys.stdin = open('input.txt', encoding='UTF-8')

ans = 0
for _ in range(10):
    num = int(input())
    if ans + num <= 100:
        ans += num
    else:
        if 100 - ans >= ans + num - 100:
            ans += num
            break
        else:
            break

print(ans)