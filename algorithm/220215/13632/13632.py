import sys
sys.stdin = open('input.txt')
# 횟수 입력받음
T = int(input())
for num in range(T):
    # A,B 두 개 따로 진행할 것이므로 변수도 따로 생성
    end, A_key, B_key = input().split()
    end_A = int(end)
    end_B = int(end)
    end = int(end)
    # 시작 지점이 1이므로 1로 지정: 이것으로 인해 아래 부분의 변화가 많음
    start_A = 1
    start_B = 1
    A_key = int(A_key)
    B_key = int(B_key)
    # 1부터 end 까지 list 생성
    arr = [int(i) for i in range(1, end + 1)]
    # binary search 횟수 기록
    cnt_A = 0
    cnt_B = 0
    # A binary search 시작
    while start_A <= end_A:
        middle_A = (start_A + end_A) // 2
        # 시작이 1부터이므로 middle_A -1 임
        if arr[middle_A-1] == A_key:
            cnt_A += 1
            break
        elif arr[middle_A-1] > A_key:
            # 시작이 1부터이므로 middle_A -1 이 아니고 middle_A 임
            end_A = middle_A
            cnt_A += 1
        else:
            # 시작이 1부터이므로 middle_A +1 이 아니고 middle_A 임
            start_A = middle_A
            cnt_A += 1
    # A와 같은 방법으로 B도 진행
    while start_B <= end_B:
        middle_B = (start_B + end_B) // 2
        if arr[middle_B-1] == B_key:
            cnt_B += 1
            break
        elif arr[middle_B-1] > B_key:
            end_B = middle_B -1
            cnt_B += 1
        else:
            start_B = middle_B +1
            cnt_B += 1
    # 조건에 따른 값 출력
    if cnt_A < cnt_B:
        print(f"#{num+1} A")
    elif cnt_A > cnt_B:
        print(f"#{num+1} B")
    else:
        print(f"#{num+1} 0")