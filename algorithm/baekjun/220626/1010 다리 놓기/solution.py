import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for _ in range(T):

    N, K = map(int, input().split())
    cnt = 0
    num1 = 1
    num2 = 1
    tmp1 = N
    while True:
        if cnt == tmp1:
            break
        num1 = num1 * N
        num2 = num2 * K
        N -= 1
        K -= 1
        cnt += 1

    print(round(num2 // num1))

# 문제 파악만 잘 하면 쉽게 풀 수 있는 문제
# 기준을 오른쪽 숫자로 두고 하는 것이 포인트