import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

# n = int(input().rstrip())
# storage = []
# for _ in range(n):
#     num = float(input().rstrip())
#     storage.append(num)

# dp = [0] * n
# dp[0] = storage[0]
# check = 0
# for i in range(1, n):
#     if storage[i] < 1:
#        dp[i] = dp[i-1]
#     else:
        


def find_maximum_product(numbers):
    max_product = numbers[0]
    current_product = numbers[0]
    
    for i in range(1, len(numbers)):
        current_product = max(numbers[i], current_product * numbers[i])
        max_product = max(max_product, current_product)
    
    return max_product

# 입력 처리
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(float(input()))

# 최댓값 출력
max_product = find_maximum_product(numbers)
print('%.3f' % max_product)

'''
소수 셋째자리까지 표현해야하기에 round 함수로 답을 나타내면 안 된다!!!!
000 같은 소숫점도 표현해야하기에 % 를 사용하여 소수 셋째자리까지 표현했다.
'''