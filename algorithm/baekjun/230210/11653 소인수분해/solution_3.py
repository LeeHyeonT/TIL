import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
N_root = int(N**0.5)+1
divisor_array = []
standard_divisor = 2

while True:
    if N == 1 or standard_divisor > N_root + 1:
        break
    if N % standard_divisor == 0:
        divisor_array.append(standard_divisor)
        N = N // standard_divisor
    else:
        if standard_divisor == 2:
            standard_divisor += 1
        else:
            standard_divisor += 2

for num in divisor_array:
    print(num)
if N != 1:
    print(N)

'''
solution_2 에서 한 발짝 더 나아갔다
소수인지를 계산할 때 판단하고자 하는 숫자의 제곱근까지만 알아보면 되는 성질을 활용하여
만약 divisor 가 N_root +1(보정) 보다 크다면 나누는 것을 중지하고 남은 N 자체가 소수가 되기에 그것을 print 해준다.
이러면 탐색하는 시간을 대폭 줄일 수 있다!!!
메모리 31256KB	시간 48ms
'''