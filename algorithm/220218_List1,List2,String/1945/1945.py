import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# 4. 소인수분해하는 함수 로직을 만듦
def factorization(number):
    lst = [0] * 5
    # 2로 나누는 경우
    while number % 2 == 0:
        if number % 2 == 0:
            lst[0] += 1
            number = number //2
    # 3으로 나누는 경우
    while number % 3 == 0:
        if number % 3 == 0:
            lst[1] += 1
            number = number //3
    # 5로 나누는 경우
    while number % 5 == 0:
        if number % 5 == 0:
            lst[2] += 1
            number = number //5
    # 7로 나누는 경우
    while number % 7 == 0:
        if number % 7 == 0:
            lst[3] += 1
            number = number //7
    # 11로 나누는 경우
    while number % 11 == 0:
        if number % 11 == 0:
            lst[4] += 1
            number = number //11

    return lst
# 1. test case 갯수 받아옴
T = int(input())
# 2. test case 만큼 반복
for tc in range(1, T+1):
    number = int(input())
    # 3. 소인수분해할 함수를 명명함
    result = factorization(number)

    print(f"#{tc}", *result)