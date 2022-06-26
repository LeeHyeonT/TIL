import sys
sys.stdin = open('input.txt', encoding='UTF-8')
from decimal import Decimal

N, K = map(int, input().split())
cnt = 0
num1 = 1
num2 = 1
tmp1 = K
while True:
    if cnt == tmp1:
        break
    num1 = num1 * N
    num2 = num2 * K
    N -= 1
    K -= 1
    cnt += 1

a =(num1 // num2)

print(Decimal((a % 10007)))

# 파이썬의 부동소수점 처리 방식 생각!
# a 구할 때 num1 / num2 로 하게되면 type이 float가 되어버려 아래 계산에서 오차 발생
# Decimal 은 굳이 안 써도 답이 나온다!