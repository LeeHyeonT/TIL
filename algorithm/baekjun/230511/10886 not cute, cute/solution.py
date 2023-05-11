import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
ans = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        ans -= 1
    else:
        ans += num

if ans > 0:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')