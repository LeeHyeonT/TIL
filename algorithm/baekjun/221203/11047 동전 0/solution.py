import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N, Target = map(int, input().split())

money_value = []
for _ in range(N):
    value = int(input())
    money_value.append(value)
money_value.reverse()
count = 0
index = 0
'''
하나하나 빼서 계산하는 경우에는
python3 으로는 시간초과가 나온다
하지만 이렇게 몫으로 계산하는 경우에는
python3 으로도 68ms 의 시간밖에 안 걸리고 메모리도 훨씬 적게 차지한다!
'''
while True:
    if index == N:
        break
    if Target >= money_value[index] and Target // money_value[index] != 0:
        # print(index)
        quotient = Target // money_value[index]
        count += quotient
        Target -= money_value[index] * quotient
    else:
        index += 1
print(count)
