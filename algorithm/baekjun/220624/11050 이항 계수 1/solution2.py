import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# while문을 1개로 줄인다면??

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

print(round(num1 / num2))

# while문 1개로 하니까 된다!
# 왜 그럴까??