import sys
sys.stdin = open('input.txt')
# 입력 횟수 받음
T = int(input())
# 입력 횟수만큼 진행
for num in range(T):
    # N, K값 받아서 정수화
    N, K = input().split()
    N = int(N)
    K = int(K)
    # 1~12 까지의 숫자를 원소로 하는 집합 생성
    arr = [int(i) for i in range(1, 13)]
    # 조건에 맞는 것 세기 위한 cnt 생성
    cnt = 0
    # 비트 연산자 생성하여 부분집합 생성
    for i in range(2 ** 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(arr[j])
        # 조건에 맞는 부분집합 찾아서 cnt 늘려줌
        if len(subset) == N:
            if sum(subset) == K:
                cnt += 1
    print(f"#{num + 1} {cnt}")

