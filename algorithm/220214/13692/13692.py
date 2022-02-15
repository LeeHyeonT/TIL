import sys
sys.stdin = open('input.txt')

# 횟수 입력
T = int(input())
for num in range(T):
    arr = []
    arr += list(map(int, input().split()))
    # 비트 연산자 이용해서 부분집합 생성
    n = len(arr)
    for i in range(1 << n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += arr[j]
            # 공집합도 부분집합 합을 0으로 계산하므로 그것을 막기 위해
            # 공집합인 i 가 1인 경우 임의의 값을 설정(여기서는 1로 설정)
            # 하여 오류를 막음
            elif i == 0:
                subset_sum = 1
        if subset_sum == 0:
            print(f"#{num+1} 1")
            break
    else:
        print(f"#{num+1} 0")

