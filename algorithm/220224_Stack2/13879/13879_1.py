import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')


# 토너먼트는 이렇게 하는 게 맞지만 문제와는 다른 방법임....
def tournament(std_number):
    global new_std_number

    if len(new_std_number) == 1:
        return new_std_number

    new_std_number = []
    # 가위바위보 하는 과정
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

    if len(std_number) % 2 != 0:
        new_std_number.append(std_number[-1])

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
