import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = input()
if int(N) < 10:
    N = N + '0'
root = ''
target = 0
count = 0
while True:
    if N == 0:
        print(1)
        break
    elif root == N:
        print(count)
        break
    if count == 0:
        for i in N:
            target += int(i)
    else:
        for i in root:
            target += int(i)

    if target >= 10:
        target = target % 10

    if count == 0:
        root = N[1] + str(target)
    else:
        root = root[1] + str(target)
    count += 1
    target = 0

'''
열심히 조건을 따라가면 되는 문제
이런 문제는 실수 없이 맞춰줘야한다!
시간이 25분이나 걸린 건 왜일까...
'''