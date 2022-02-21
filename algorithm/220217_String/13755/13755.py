import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = int(input())
for num in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    arr = [list(input()) for _ in range(N)]

    # 가로 탐색
    for i in range(N):
        for j in range(N - M + 1):
            text = ""
            for k in range(M):
                text += arr[i][j+k]

            if text == text[::-1]:
                print(f"#{num+1} {text}")
                break

    # 세로 탐색
    for i in range(N):
        for j in range(N - M + 1):
            text = ""
            for k in range(M):
                text += arr[j+k][i]
            if text == text[::-1]:
                print(f"#{num + 1} {text}")
                break

