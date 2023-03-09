import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 3차원 배열을 이용한 풀이
def w(a, b, c, dp):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, dp)

    if dp[a][b][c] != None:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1, dp) + w(a, b-1, c-1, dp) - w(a, b-1, c, dp)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c, dp) + w(a-1, b-1, c, dp) + w(a-1, b, c-1, dp) - w(a-1, b-1, c-1, dp)
    return dp[a][b][c]

# 입력을 받습니다.
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    # 배열을 초기화합니다. None으로 초기화하면 함수 내에서 이전에 계산한 값인지 아닌지를 구별할 수 있습니다.
    dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

    result = w(a, b, c, dp)
    print(f"w({a}, {b}, {c}) = {result}")