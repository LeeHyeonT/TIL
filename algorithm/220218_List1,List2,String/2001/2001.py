import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 갯수만큼 입력받음
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sol = 0
    # arr 의 행 갯수 - 합해줄 값들의 행 갯수 + 1 해서 진행
    for i in range(N-M+1):
        # arr 의 열 갯수 - 합해줄 값들의 열 갯수  + 1 해서 진행
        for j in range(N-M+1):
            # 구할 값 초기화
            sol = 0
            # M 길이만큼 값 더해줘야하므로 범위를 M으로 설정(행)
            for k in range(M):
                # M 길이만큼 값 더해줘야하므로 범위를 M으로 설정(열)
                for l in range(M):
                    sol += arr[i+k][j+l]
            # 최댓값 구하기
            if max_sol < sol:
                max_sol = sol

    print(f"#{tc} {max_sol}")