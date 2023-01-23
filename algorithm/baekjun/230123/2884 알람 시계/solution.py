import sys
sys.stdin = open('input.txt', encoding='UTF-8')

H, M = map(int, input().split())

if M < 45:
    answer_M = 60 + M - 45
    if H == 0:
        answer_H = 23
    else:
        answer_H = H - 1
else:
    answer_M = M - 45
    answer_H = H

print(answer_H, answer_M)

'''
조건만 잘 따지면 안 틀리고 한 번에 맞출 수 있는 문제
'''