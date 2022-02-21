import sys
sys.stdin = open('input.txt')
# 같은 색끼리 겹칠 수 있는 경우
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

        # 색이 파란색인 경우 해당 arr idx 에 j씩 더해줌
        elif color == 2:
            for r in range(r2, r1 - 1, -1):
                for c in range(c2, c1 - 1, -1):
                    # 일부러 순허수값을 더해줌, 이후 계산에서 사용하기 위해
                    arr[r][c] += (0 + 1j)

    # 순허수(파란색만 존재), 순정수(빨간색만 존재)인 경우를 제외하고 count 를 더함
    cnt = 0
    for j in arr:
        for k in j:
            if type(k) == complex and k.real != 0:
                cnt += 1

    print(f"#{num+1} {cnt}")