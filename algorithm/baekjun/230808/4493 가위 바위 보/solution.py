import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    vs = int(input())
    score_p1 = 0
    score_p2 = 0
    for _ in range(vs):
        p1, p2 = map(str, input().rstrip().split())
        if p1 == 'R':
            if p2 == 'S':
                score_p1 += 1
            elif p2 == 'P':
                score_p2 += 1
        elif p1 == 'S':
            if p2 == 'P':
                score_p1 += 1
            elif p2 == 'R':
                score_p2 += 1
        else:
            if p2 == 'R':
                score_p1 += 1
            elif p2 == 'S':
                score_p2 += 1
    
    if score_p1 > score_p2:
        print('Player 1')
    elif score_p1 < score_p2:
        print('Player 2')
    else:
        print('TIE')

'''
readline 사용하지 않았을 시 걸리는 시간: 2088ms
readline 사용 시 걸리는 시간: 84ms
readline + 함수 만들어 사용 시 걸리는 시간: 대략 68ms
'''