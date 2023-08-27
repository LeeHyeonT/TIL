import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
n = int(input())
score = list(input().rstrip())
ans = 0
bonus = 0
for i in range(n):
    if score[i] == 'O':
        ans += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(ans)

'''
문제를 잘 읽을 것
'''