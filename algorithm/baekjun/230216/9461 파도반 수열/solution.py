import sys 
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for _ in range(T):
    N = int(input())
    if N <= 3:
        print(1)
    elif N <= 5:
        print(2)
    else:
        padovan_array = [0] * N
        # 기본 세팅
        padovan_array[0] = 1
        padovan_array[1] = 1
        padovan_array[2] = 1
        padovan_array[3] = 2
        padovan_array[4] = 2

        for i in range(5, N):
            padovan_array[i] = padovan_array[i-1] + padovan_array[i-5]
        
        print(padovan_array[N-1])

'''
초기 조건 잘 생각하여 만드는 문제
N 값이 무조건 6 이상은 아니기에 위와 같이 코드를 짰다면 그 앞의 부분에 대한 처리가 반드시 필요함
'''