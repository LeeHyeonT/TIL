'''
1) itertools 내의 product 사용
중복순열을 바로 계산할 수 있는 내장 함수를 사용한다.
하지만 딱히 효율적인 것 같지는 않다.
'''
# import sys
# sys.stdin = open('input.txt', encoding='UTF-8')
# from itertools import product

# N, M = map(int, input().split())
# standard_list = []
# for i in range(1, N+1):
#     standard_list.append(i)
# answer = list(product(standard_list, repeat= M))

# for numbers in answer:
#     for number in numbers:
#         print(number, end=' ')
#     print('')

'''
2) 중복순열 구현하기
backtracking 을 활용하여 직접 구현한다.
위의 방식보다 시간은 약 2/5, 메모리는 약 3/11 배 소요된다!
'''
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())
standard_array = []

def Product(N, M, start):
    if len(standard_array) == M:
        print(' '.join(map(str, standard_array)))
        return
    for i in range(start, N+1):
        standard_array.append(i)
        Product(N, M, start)        # 이 부분이 핵심! start 값이 계속 같다고 할 수도 있지만 for문을 돌며 차례차례 값들이 더해지는 방식이다!
        standard_array.pop()

Product(N, M, 1)