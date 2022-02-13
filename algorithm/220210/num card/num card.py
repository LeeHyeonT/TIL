# import sys
# sys.stdin = open(input.txt)

# 몇 번 실행할건지 값 받아옴
T = int(input())
for num in range(T):
    # 받아올 숫자 갯수, 숫자 입력
    N = int(input())
    card_num = list(map(int, input()))
    # 숫자 count 하는 리스트 생성
    cnt = [0] * 10
    # 숫자 count 하여 값 넣어줌
    for i in range(N):
        cnt[card_num[i]] += 1
    # 빈도수 가장 큰 값, 그 빈도수를 가지는 숫자 생성
    max_num = 0
    for j in range(10):
        if cnt[j] >= cnt[max_num]:
            max_cnt = cnt[j]
            max_num = j

    print(f"#{num+1} {max_num} {max_cnt}")