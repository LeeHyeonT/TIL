import sys
sys.stdin = open('input.txt', encoding='UTF-8')

t = int(input())
for _ in range(t):
    scoring_board = [0, 0]
    for _ in range(9):
        y, k = map(int, input().split())
        scoring_board[0] += y
        scoring_board[1] += k
    
    if scoring_board[0] > scoring_board[1]:
        print('Yonsei')
    elif scoring_board[0] < scoring_board[1]:
        print('Korea')
    else:
        print('Draw')