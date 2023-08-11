import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 후보의 수 N 입력
N = int(input())
if N == 1:
    print(0)
else:
    # 각 후보별 득표수 입력받아 리스트에 저장
    votes = []
    for _ in range(N):
        votes.append(int(input()))

    # 다솜이의 득표수 (기호 1번 후보)
    dosom_votes = votes[0]

    # 매수해야 하는 숫자의 최솟값 계산
    min_buy_number = 0

    # 다솜이의 득표수가 다른 후보보다 작은 경우에만 매수가 필요함
    if dosom_votes <= max(votes[1:]):
        # 다솜이를 제외한 후보 중 매수해야 하는 숫자 계산
        while dosom_votes <= max(votes[1:]):
            # 다솜이보다 득표수가 큰 후보 중 가장 큰 득표수를 가진 후보의 인덱스
            max_index = votes.index(max(votes[1:]))

            # 가장 큰 득표수를 가진 후보의 득표수를 줄임
            votes[max_index] -= 1

            # 다솜이의 득표수를 증가
            dosom_votes += 1

            # 매수해야 하는 숫자 카운트 증가
            min_buy_number += 1

    # 결과 출력
    print(min_buy_number)






