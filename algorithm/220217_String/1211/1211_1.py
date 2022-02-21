import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

t = 10
for _ in range(t):
    input()
    board = []
    for i in range(100):
        lis = list(map(int, input().split()))
        board.append(lis)

    min_len = 10000
    answer = 0
    for i in range(100):
        if not board[0][i]:
            continue
        x = i
        y = 0
        cnt = 1
        while y < 100:

            if x != 0 and board[y][x - 1] == 1:
                while x >= 0 and board[y][x] == 1:
                    cnt += 1
                    x -= 1
                x += 1
                cnt -= 1
            elif x != 99 and board[y][x + 1] == 1:
                while x < 100 and board[y][x] == 1:
                    cnt += 1
                    x += 1
                x -= 1
                cnt -= 1

            cnt += 1
            y += 1
        if min_len > cnt:
            min_len = cnt
            answer = i

    print(f'#{_ + 1} {answer} ')