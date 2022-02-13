import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    num_str = list(map(int, input().split()))
    # 숫자 배열에서의 합 저장할 list 생성
    sum_lst = [0]*(N-M+1)
    # 숫자 배열에서의 합 저장
    for i in range(N-M+1):
        sum_num = 0
        # 앞에서부터 M 개까지의 숫자들 더하여 sum_num 에 저장
        for j in range(i, i+M):
            sum_num += num_str[j]
        # 앞에서 구한 sum_num 을 sum_lst 안에 저장
        sum_lst[i] += sum_num
        
    # bubble 정렬 이용해서 sum_lst 내의 값 오름차순 정렬
    for bub in range(N-M+1-1, 0, -1):
        for i in range(0, bub):
            if sum_lst[i] > sum_lst[i+1]:
                sum_lst[i], sum_lst[i+1] = sum_lst[i+1], sum_lst[i]
            continue

    print(f"#{num + 1} {sum_lst[-1] - sum_lst[0]}")
    #     print(sum_num)
    #     print(last_sum_num)
    #     if last_sum_num > sum_num:
    #         sum_max = last_sum_num
    #     if last_sum_num < sum_num:
    #         sum_min = last_sum_num
    #     last_sum_num = sum_num
    # print(sum_max)
    # print(sum_min)

