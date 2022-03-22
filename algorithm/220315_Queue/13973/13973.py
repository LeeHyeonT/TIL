import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [([0]*M) for _ in range(3)]

    cheese = list(map(int, input().split()))
    # 배열에 피자 번호, 치즈 양, (이따 사용할) 카운트 --> 3가지를 각각 한 행에 지정해서 저장함
    for i in range(M):
        arr[0][i] = i+1
        arr[1][i] = cheese[i]
        arr[2][i] = 0
    print(arr)
    # queue 생성: N 개만큼의 피자 번호, 치즈 양, 카운트 받아옴
    q = [[0] * N for _ in range(3)]
    for j in range(N):
        q[0][j] = (arr[0][j])
        q[1][j] = (arr[1][j])

    # 자리바꾸기 시작
    j = N
    while True:
        # 한 번 자리바꾸는 과정
        tmp0 = q[0][0]      # 피자번호
        tmp1 = q[1][0]      # 치즈양
        tmp2 = q[2][0]      # 도는 것 카운트
        q[0].pop(0)
        q[1].pop(0)
        q[2].pop(0)
        q[0].append(tmp0)
        q[1].append(tmp1)
        q[2].append(tmp2)

        # 한 번 자리바꿨으니 카운트 1개씩 올려줌
        for k in range(N):
            if q[2][k] is None:
                continue
            q[2][k] += 1
            # 카운트가 N 이상이 되면 치즈 양 절반으로 줄고 카운트 0으로 초기화
            if q[2][k] >= N:
                q[1][k] = q[1][k] // 2
                q[2][k] = 0

        # 첫 번째 자리 피자의 치즈 양이 0이라면 다음 피자와 교체
        if q[1][0] == 0:
            # # 피자 있는 거 다 넣으면 더이상 넣을 피자 없으므로 피자 넣을 공간 제거
            # # 공간 제거하는 문제였으면 이렇게 해야했지만 이 문제는 그게 아닌걸...
            # if j >= M:
            #     q[0].pop(0)
            #     q[1].pop(0)
            #     q[2].pop(0)
            #     N -= 1

            # 더이상 넣을 피자 없으면 그 공간 비워둠
            if j >= M:
                q[0][0] = None
                q[1][0] = -1
                q[2][0] = None
            else:
                # 교체작업
                q[0][0] = arr[0][j]
                q[1][0] = arr[1][j]
                q[2][0] = 0
                j += 1

        print(q)
        # 비워둔 공간이 전체 공간 -1 이라면 피자 1개 남은 것이므로 반복 종료
        if q[0].count(None) == N-1:
            break
    # 이름 저장해놓은 곳 순회하면서 None 아닌 값 찾아서 도출

    res = 0
    for m in range(N):
        if q[0][m] is not None:
            res = q[0][m]

    print(f"#{tc} {res}")





