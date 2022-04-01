import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# 이 방법은 실패한 방법!!!
# 토너먼트는 이렇게 하는 게 맞지만 문제와는 다른 방법임....
def tournament(std_number):
    global new_std_number

    if len(new_std_number) == 1:
        return new_std_number

    new_std_number = []
    # 가위바위보 하는 과정
    # 남은 학생수를 4로 나눴을 때의 나머지값에 따라 과정이 조금 다름
    
    # 1) 나머지 0 (가장 깔끔한 상황)
    if len(std_number) % 4 == 0:
        for k in range(0, len(std_number) // 2):
            a = std_number[2 * k][1]
            b = std_number[2 * k + 1][1]
            if a > b:
                if a == 3 and b == 1:
                    new_std_number.append(std_number[2 * k + 1])
                else:
                    new_std_number.append(std_number[2 * k])
            elif a == b:
                new_std_number.append(std_number[2 * k])
            elif a < b:
                if a == 1 and b == 3:
                    new_std_number.append(std_number[2 * k])
                else:
                    new_std_number.append(std_number[2 * k + 1])
    # 2) 나머지 1 
    # 좌 우 갯수가 2 3 / 4 5 이런 식으로 왼쪽은 짝수개, 오른쪽은 홀수개로 나뉨
    elif len(std_number) % 4 == 1:
        for k in range(0, len(std_number) // 2):
            a = std_number[2 * k][1]
            b = std_number[2 * k + 1][1]
            if a > b:
                if a == 3 and b == 1:
                    new_std_number.append(std_number[2 * k + 1])
                else:
                    new_std_number.append(std_number[2 * k])
            elif a == b:
                new_std_number.append(std_number[2 * k])
            elif a < b:
                if a == 1 and b == 3:
                    new_std_number.append(std_number[2 * k])
                else:
                    new_std_number.append(std_number[2 * k + 1])
        # 오른쪽 끝에 하나 남는 거 더해줌
        new_std_number.append(std_number[-1])
        
    # 3) 4로 나눈 나머지가 2인 경우
    # 좌 우 갯수가 3 3 / 5 5 처럼 둘 다 홀수개
    elif len(std_number) % 4 == 2:
        for k in range(0, len(std_number) // 2):
            a = std_number[2 * k][1]
            b = std_number[2 * k + 1][1]
            if a > b:
                if a == 3 and b == 1:
                    new_std_number.append(std_number[2 * k + 1])
                else:
                    new_std_number.append(std_number[2 * k])
            elif a == b:
                new_std_number.append(std_number[2 * k])
            elif a < b:
                if a == 1 and b == 3:
                    new_std_number.append(std_number[2 * k])
                else:
                    new_std_number.append(std_number[2 * k + 1])
    print(new_std_number)
    tournament(new_std_number)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    std_number = [[i] for i in range(1, N + 1)]

    number = list(map(int, input().split()))
    for j in range(len(number)):
        std_number[j].append(number[j])
        std_number[j] = tuple(std_number[j])

    new_std_number = []
    tournament(std_number)

    print(f"#{tc} {new_std_number[0][0]}")
