import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# dictionary 를 이용한 풀이 방법: 시간 초과...
# list 탐색보다 dictionary 탐색의 시간이 더 오래 걸리기에 일어나는 문제
def w(a, b, c, memo):
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        memo[(a, b, c)] = 1
        return 1

    if a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = w(20, 20, 20, memo)
        return memo[(a, b, c)]

    if a < b and b < c:
        memo[(a, b, c)] = w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
        return memo[(a, b, c)]

    memo[(a, b, c)] = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
    return memo[(a, b, c)]

# 입력을 받습니다.
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    # Memoization에 사용할 딕셔너리를 초기화합니다.
    memo = {}

    result = w(a, b, c, memo)
    print(f"w({a}, {b}, {c}) = {result}")