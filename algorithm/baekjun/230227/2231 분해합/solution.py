import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())  # 자연수 N 입력 받기

# N의 분해합을 계산하는 함수
def decomposition_sum(num):
    sum = num
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

# 1부터 N까지 모든 수에 대해 생성자 찾기
for i in range(1, n+1):
    if decomposition_sum(i) == n:
        print(i)
        break
else:
    print(0)

'''
100만의 반복까지는 1초 내로 끊을 수 있으므로 이런 코드를 작성하여 문제를 푸는 것이 가능하다
모든 경우를 다 돌아보는 Brute Force 알고리즘 문제
'''