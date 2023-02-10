import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
divisor_array = []
standard_divisor = 2
while True:
    if N == 1:
        break
    if N % standard_divisor == 0:
        divisor_array.append(standard_divisor)
        N = N // standard_divisor
    else:
        standard_divisor += 1

for num in divisor_array:
    print(num)

'''
가장 담백한 방법
그냥 2부터 쭈욱 올라가며 나눠주고 진행한다.
하지만 효율적인 방법은 아니다.
메모리 31256KB	시간 1284ms
'''