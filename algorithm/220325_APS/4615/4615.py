import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # 초기 오델로판 설정
    arr = [[0]*N for _ in range(N//2 - 1)]
    arr.append([0]* (N//2 -1) + [2,1] + [0]* (N//2 -1))
    arr.append([0]* (N//2 -1) + [1,2] + [0]* (N//2 -1))
    for _ in range(N//2 - 1):
        arr.append([0]*N)
        
    print(arr)
    # for i in range(M):
    #     if i <= 2:
