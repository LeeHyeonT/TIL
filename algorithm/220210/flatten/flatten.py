import sys
sys.stdin = open('input.txt')

for num in range(10):
    tst_num = int(input())
    height_lst = list(map(int, input().split()))
    for _ in range(tst_num):
        # bubble 정렬 실행
        for bub in range(100-1, 0, -1):
            for j in range(0, bub):
                if height_lst[j] >= height_lst[j + 1]:
                    height_lst[j], height_lst[j + 1] = height_lst[j + 1], height_lst[j]
                continue
        # 정렬 후 맨 처음 값에 +1, 맨 마지막 값에 -1 / 맨 처음값과 맨 마지막 값의 차이가 1 이하인 경우 for 문 탈출
        if height_lst[-1] - height_lst[0] <= 1:
            break
        height_lst[-1] -= 1
        height_lst[0] += 1

    # 값 구하기 전에 다시 bubble 정렬해야 마지막으로 +1 -1 한 값 반영할 수 있음
    for bub in range(100 - 1, 0, -1):
        for j in range(0, bub):
            if height_lst[j] >= height_lst[j + 1]:
                height_lst[j], height_lst[j + 1] = height_lst[j + 1], height_lst[j]
            continue

    print(f"#{num+1} {height_lst[-1] - height_lst[0]}")
