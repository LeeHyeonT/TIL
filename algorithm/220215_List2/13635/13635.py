import sys
sys.stdin = open('input.txt')

T = int(input())
for n in range(T):
    length = int(input())
    num = list(map(int, input().split()))

    # 받아온 값 내림차순 정렬 by bubble sort
    for bub in range(length-1, 0, -1):

        for i in range(0, bub):
            if num[i] < num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
            continue

    # 특수 정렬 담을 리스트 생성 및 진행
    lst = []
    for i in range(length//2 + 1):
        # idx 0일 때는 idx = -idx 이므로 한 번만 추가
        if i == 0:
            lst.append(num[i])
        # 짝수 개인 경우 마지막이 겹치므로 한 번만 추가
        elif num[-i] == num[i]:
            lst.append(num[i])
        else:
            lst.append(num[-i])
            lst.append(num[i])

    # 10개만 출력해야하므로 10개 담을 list 생성
    list_10 = []
    for i in range(10):
        list_10.append(lst[i])

    print(f"#{n+1}", *list_10)