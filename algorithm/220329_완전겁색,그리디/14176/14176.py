import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start_lst = []
    end_lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        start_lst.append(s)
        end_lst.append(e)
    print(start_lst, end_lst)

    cnt = 0
    idx = 0
    start_time = 0
    while True:
        start_time = min(end_lst)
        idx = end_lst.index(start_time)
        end_lst.pop(idx)
        start_lst.pop(idx)
        cnt += 1

