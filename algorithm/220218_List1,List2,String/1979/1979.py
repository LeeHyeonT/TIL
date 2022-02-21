import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 만큼 입력받음
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 각 행의 끝에 0 을 붙여줘 계산을 용이하게함
    arr = [list(map(int, input().split()))+[0] for _ in range(N)]
    # 마찬가지로 0으로 이루어진 행을 하나 추가하여 계산을 용이하게함
    arr += [[0]*(N+1)]
    cnt = 0
    # 행 계산
    for i in range(N):
        for j in range(N-K+1):
            if j >= 1:
                if arr[i][j:j+K] == [1]*K and arr[i][j+K] != 1 and arr[i][j-1] != 1:
                    cnt += 1
            else:
                if arr[i][j:j+K] == [1]*K and arr[i][j+K] != 1:
                    cnt += 1
    # 전치행렬: 행과 열을 뒤집어줌
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # 행 계산과 식이 같지만 그 결과는 본래의 것의 열 계산임!
    for i in range(N):
        for j in range(N-K+1):
            if j >= 1:
                if arr[i][j:j+K] == [1]*K and arr[i][j+K] != 1 and arr[i][j-1] != 1:
                    cnt += 1
            else:
                if arr[i][j:j+K] == [1]*K and arr[i][j+K] != 1:
                    cnt += 1

    print(f"#{tc} {cnt}")
