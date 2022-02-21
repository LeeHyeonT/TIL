# 몇 번 실행할건지 결정
T = int(input())
for num in range(T):
    # 숫자갯수, 숫자 받아옴
    N = int(input())
    lst = list(map(int, input().split()))
    # bubble정렬 이용하여 오름차순으로 lst 내 값들 정리
    for bub in range(N-1, 0, -1):

        for i in range(0, bub):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            continue

    print(f"#{num+1} {lst[-1] - lst[0]}")


# import sys
# sys.stdin = open(input.txt)