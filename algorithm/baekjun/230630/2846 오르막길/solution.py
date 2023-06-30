import sys
sys.stdin  = open('input.txt', encoding='UTF-8')

n = int(input())
ways = list(map(int, input().split()))
nominee = 0
ans = 0
for i in range(1, n):
    if ways[i] > ways[i-1]:
        nominee += ways[i] - ways[i-1]
    else:
        if ans < nominee:
            ans = nominee
            nominee = 0
        else:
            nominee = 0
else:
        if ans < nominee:
            ans = nominee
            
print(ans)