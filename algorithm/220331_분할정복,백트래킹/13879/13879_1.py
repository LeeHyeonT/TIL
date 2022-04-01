import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# 문제에 나와있는 조건에 맞게 짝 지어 토너먼트 준비하는 함수
def coupling(std_number):
    global coupling_lst
    # 짝을 지었거나 혼자 남았다면 그 값을 넘겨줌
    if len(std_number) == 1 or len(std_number) == 2:
        coupling_lst.append(std_number)
        return
    # 홀수 길이
    if len(std_number) % 2:
        std_number_half1 = std_number[:len(std_number) // 2 + 1]
        std_number_half2 = std_number[len(std_number) // 2 + 1:]
        # 계속 짝 지어 2명 / 1명 나올 때까지 진행
        coupling(std_number_half1)
        coupling(std_number_half2)
    # 짝수 길이
    else:
        std_number_half1 = std_number[:len(std_number)//2]
        std_number_half2 = std_number[len(std_number)//2:]
        # 계속 짝 지어 2명 / 1명 나올 때까지 진행
        coupling(std_number_half1)
        coupling(std_number_half2)

    return coupling_lst

# 문제에 나와있는 룰에 맞춰서 토너먼트 진행하는 함수
def tournament(lst):
    global new_std_number
    for k in range(0, len(lst)):
        # 승자가 정해지면 새로운 리스트에 넣어줌
        if len(lst[k]) == 1:
            new_std_number.append(lst[k][0])
            continue
        a = lst[k][0][1]
        b = lst[k][1][1]
        if a > b:
            if a == 3 and b == 1:
                new_std_number.append(lst[k][1])
            else:
                new_std_number.append(lst[k][0])
        elif a == b:
            new_std_number.append(lst[k][0])
        elif a < b:
            if a == 1 and b == 3:
                new_std_number.append(lst[k][0])
            else:
                new_std_number.append(lst[k][1])

# 짝 지어 토너먼트 하는 것 반복하는 함수
def reputation(lst):
    global coupling_lst
    global new_std_number
    while True:
        coupling(lst)
        tournament(coupling_lst)
        # 계속 진행하여 최후의 1인이 정해지면 그 학생 번호 출력
        if len(new_std_number) == 1:
            print(f"#{tc} {new_std_number[0][0]}")
            return
        lst = new_std_number
        # 반복할 때마가 이 두 가지 값 초기화해줘야 함
        coupling_lst = []
        new_std_number = []


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    std_number = [[i] for i in range(1, N + 1)]
    # 학생 번호와 학생이 가진 카드 번호를 tuple 로 묶어 표현함
    number = list(map(int, input().split()))
    for j in range(len(number)):
        std_number[j].append(number[j])
        std_number[j] = tuple(std_number[j])

    coupling_lst = []
    new_std_number = []
    reputation(std_number)
    # print(std_number)
    # coupling_lst = []
    # coupling(std_number)
    # print(coupling_lst)
    # new_std_number = []
    # tournament(coupling_lst)
    # print(new_std_number)
