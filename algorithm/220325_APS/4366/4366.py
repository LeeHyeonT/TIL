import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# def func(string):
#     tmp = 0
#     k = 1
#     while k < 3:
#         string = str((int(string) + k) % 3)
#         for j in range(len(num3_lst)):
#             tmp += (int(num3_lst[j]) * (3 ** (len(num3_lst) - 1 - j)))
#         num3_10.append(tmp)
#         k += 1

# 3진수의 경우 그냥 함수로 각각의 자릿수가 0, 1, 2로 변할 때를 표현함
# 값을 0으로 변경 후 10진수로 바꿈
def func_0():
    tmp = 0
    # copy 해서 사용해야 원본 유지하면서 각 자리 하나씩만 변화 가능
    num3_lst_copy = num3_lst[:]
    num3_lst_copy[num] = str(0)
    for j in range(len(num3_lst_copy)):
        tmp += (int(num3_lst_copy[j]) * (3 ** (len(num3_lst_copy) - 1 - j)))
    # 가지치기: 일단 2진수를 10진수로 바꾼 값을 저장해놨기 때문에 그 값이랑 일치하는 게 있으면 중단 가능
    if tmp in num2_10:
        return print(f"#{tc} {tmp}")
    num3_10.append(tmp)

# 값을 1로 변경 후 10진수로 바꿈
def func_1():
    tmp = 0
    num3_lst_copy = num3_lst[:]
    num3_lst_copy[num] = str(1)
    for j in range(len(num3_lst_copy)):
        tmp += (int(num3_lst_copy[j]) * (3 ** (len(num3_lst_copy) - 1 - j)))
    if tmp in num2_10:
        return print(f"#{tc} {tmp}")
    num3_10.append(tmp)

# 값을 2로 변경 후 10진수로 바꿈
def func_2():
    tmp = 0
    num3_lst_copy = num3_lst[:]
    num3_lst_copy[num] = str(2)
    for j in range(len(num3_lst_copy)):
        tmp += (int(num3_lst_copy[j]) * (3 ** (len(num3_lst_copy) - 1 - j)))
    if tmp in num2_10:
        return print(f"#{tc} {tmp}")
    num3_10.append(tmp)

T = int(input())
for tc in range(1, T+1):
    # 2진수 받아오고 각 자리값 쉽게 변경하기위해 list 안에 한 자리씩 넣어놓음
    num2 = input()
    num2_lst = []
    for num in num2:
        num2_lst.append(num)
    # 3진수도 마찬가지
    num3 = input()
    num3_lst = []
    for num in num3:
        num3_lst.append(num)

    # 2진수의 각 자리별 숫자 변경 및 10진법으로 바꾸는 과정
    num2_10 = [0] * len(num2_lst)
    for num in range(len(num2_lst)):
        # copy 사용해야 원본 유지하여 한 자리씩만 변경 가능
        # copy 안 쓰려면 후처리 따로 해 줘야하는데 귀찮으니까...!
        num2_lst_copy = num2_lst[:]
        if num2_lst_copy[num] == str(1):
            num2_lst_copy[num] = str(0)
        else:
            num2_lst_copy[num] = str(1)

        for i in range(len(num2_lst)):
            num2_10[num] += (int(num2_lst_copy[i]) * (2**(len(num2_lst)-1-i)))

    num3_10 = []
    for num in range(len(num3_lst)):
        if num3_lst[num] == str(2):
            func_0()
            func_1()
        elif num3_lst[num] == str(1):
            func_0()
            func_2()
        else:
            func_1()
            func_2()






