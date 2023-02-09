import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num_array = list(map(int, input().split()))
operator_num = list(map(int, input().split()))

max_num = -1000000000
min_num = 1000000000

def BackTracking(index, number, past_number):
    global max_num, min_num
    if index == len(num_array):
    # if sum(operator_num) == 0:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
        return 
    for i in range(4):
        if i == 0 and operator_num[i] != 0:
            past_number = number
            number += num_array[index]
            operator_num[i] -= 1
            BackTracking(index+1, number, past_number)
            operator_num[i] += 1
            number = past_number
        elif i == 1 and operator_num[i] != 0:
            past_number = number
            number -= num_array[index]
            operator_num[i] -= 1
            BackTracking(index+1, number, past_number)
            operator_num[i] += 1
            number = past_number
        elif i == 2 and operator_num[i] != 0:
            past_number = number
            number *= num_array[index]
            operator_num[i] -= 1
            BackTracking(index+1, number, past_number)
            operator_num[i] += 1
            number = past_number
        elif i == 3 and operator_num[i] != 0:
            past_number = number
            if number < 0:
                number = -(abs(number) // num_array[index])
            else:
                number = number // num_array[index]
            operator_num[i] -= 1
            BackTracking(index+1, number, past_number)
            operator_num[i] += 1
            number = past_number

BackTracking(1, num_array[0], 0)
print(max_num)
print(min_num)

'''
전형적인 dfs / backtracking 문제
약간의 시행착오를 거쳤는데 그 이유는 backtracking 을 실행하면서 전에 바꿔놓은 것들을 돌려놓는 작업이 서툴렀기 때문
내 코드대로 진행한다면 operator_num 과 number 를 다시 원상복구시켜야 하는데 operator_num 만 원상복구시켜 답이 잘 나오지 않았음
후에 인지 후 한 단계 전 number 를 past_number 로 저장, 그 친구를 이용하여 number 를 원상복구시킴
'''