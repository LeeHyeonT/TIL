import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# dynamic programming 을 사용한 풀이 방법 2

# DP 테이블을 초기화합니다.
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

# 초기값을 설정합니다.
for i in range(21):
    for j in range(21):
        dp[0][i][j] = 1
        dp[i][0][j] = 1
        dp[i][j][0] = 1

# DP 테이블을 갱신합니다.
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

# 입력을 받습니다.
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    # a, b, c가 0보다 작으면 1을 출력합니다.
    if a <= 0 or b <= 0 or c <= 0:
        result = 1
    # a, b, c가 20보다 크면 20으로 조정합니다.
    elif a > 20 or b > 20 or c > 20:
        result = dp[20][20][20]
    else:
        result = dp[a][b][c]
    print(f"w({a}, {b}, {c}) = {result}")
    
'''
dynamic programming 만 사용하면 시간이 은근 오래 소요된다.
이 문제는 abc 의 숫자가 그리 크지 않기에 미리 dp값을 다 계산해 놓는 것보단
적당한 재귀함수를 사용하여 그 때 그 때 계산하는 것이 속도 측면에서 더 도움이 된다.
ps. thank you chatgpt!
'''