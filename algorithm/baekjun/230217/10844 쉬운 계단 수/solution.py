import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def count_steps(n):
    memo = [[0 for _ in range(10)] for _ in range(n)]
    # memo[i][j]는 길이 i + 1이고 마지막 숫자가 j인 단계 수의 개수를 저장합니다.
    for i in range(1, 10):
        memo[0][i] = 1
    for i in range(1, n):
        for j in range(10):
            if j > 0:
                memo[i][j] += memo[i-1][j-1]
            if j < 9:
                memo[i][j] += memo[i-1][j+1]
    return sum(memo[n-1]) % 1000000000

N = int(input())
steps = count_steps(N)
print(steps) 

'''
이중 리스트를 활용한 dynamic programming 문제
각 자릿수에 들어올 수 있는 숫자들(0~9) 에 대해 그 숫자로 끝나는 수를 몇 개 만들 수 있는지 계속 더해나가며 계산하는 것이 특징
'''