import sys
sys.stdin = open('input.txt', encoding='UTF-8')

winner = 0
winner_score = 0
for i in range(5):
    score = list(map(int, input().split()))
    if sum(score) > winner_score:
        winner_score = sum(score)
        winner = i + 1

print(winner, end=' ')
print(winner_score)