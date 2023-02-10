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
        if standard_divisor == 2:
            standard_divisor += 1
        else:
            standard_divisor += 2

for num in divisor_array:
    print(num)

'''
solution_1 에서 약간만 수정한 답안
소인수분해할 때 나오는 것은 결국 소수들인데 소수는 2,3 라인을 제외하고는 모두 크기가 전의 것에 비해 2 이상 차이난다
이 점을 이용하여 divisor 를 2씩 증가시켜 시간을 감소시키는 데에 성공!
메모리 31256KB	시간 768ms
'''