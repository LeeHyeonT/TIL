import sys
sys.stdin = open('input.txt')
# 몇 번 시행할 건지 입력받음
T = int(input())
for num in range(T):
    # 영역생성: 초기값 0으로 하여 10 * 10 영역 생성
    arr = [[0] * 10 for _ in range(10)]
    # 색칠을 몇 번 할 것인가 결정
    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 색이 빨간색인 경우 해당 arr idx 에 1씩 더해줌
        if color == 1:
            for r in range(r2, r1-1, -1):
                for c in range(c2, c1-1, -1):
                    arr[r][c] += 1
        # 색이 파란색인 경우 해당 arr idx 에 2씩 더해줌
        elif color == 2:
            for r in range(r2, r1 - 1, -1):
                for c in range(c2, c1 - 1, -1):
                    arr[r][c] += 2
    # 겹친 부분 새는 과정: 같은 색은 안 겹치므로 빨강+파랑 = 3의 값이 나올 것
    # 따라서 arr 요소들 중 값이 3인 것들만 count 하여 진행
    cnt = 0
    for j in arr:
        for k in j:
            if k == 3:
                cnt += 1

    print(f"#{num+1} {cnt}")