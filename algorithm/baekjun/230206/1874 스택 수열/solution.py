import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n = int(input())
standard_array = []
stack_array = []
answer_array = []
pm_array = []
for _ in range(n):
    standard_array.append(int(input()))

standard_array_index = 0
stack_array_exit = -1
plus_num = 0
while True:
    if len(answer_array) == n:
        break
    if len(stack_array) == 0:
        while True:
            plus_num += 1
            stack_array.append(plus_num)
            pm_array.append('+')
            stack_array_exit += 1
            if standard_array[standard_array_index] == stack_array[stack_array_exit]:
                break

    if standard_array[standard_array_index] > stack_array[stack_array_exit]:
        while True:
            if standard_array[standard_array_index] == stack_array[stack_array_exit]:
                answer_array.append(stack_array.pop())
                pm_array.append('-')
                standard_array_index += 1
                stack_array_exit -= 1
                break
            plus_num += 1
            stack_array.append(plus_num)
            pm_array.append('+')
            stack_array_exit += 1

    elif standard_array[standard_array_index] < stack_array[stack_array_exit]:
        break

    elif standard_array[standard_array_index] == stack_array[stack_array_exit]:
        answer_array.append(stack_array.pop())
        pm_array.append('-')
        standard_array_index += 1
        stack_array_exit -= 1
  
if len(answer_array) == n:
    for pm in pm_array:
        print(pm)
else:
    print('NO')
    
'''
처음 stack_array 에 값이 없을 때 for 문을 통해 적당한 지점까지 숫자를 더하는 식으로
진행했는데 그렇게 하면 다음과 같은 문제가 발생한다.
3 2 1 4 .... 같은 수열의 경우 stack_array 의 길이가 0인 상황이 한 번 이상 나오는데
for 문을 통해 숫자를 더한다면 계속 많은 숫자가 더해지게되어 틀린 답이 도출된다.

따라서 더해야하는 값은 정해져있기에 그 값(plus_num)을 계속 체크하며 나아가는 방식으로 진행하였다.

'''