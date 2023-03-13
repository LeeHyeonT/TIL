import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
balls = list(map(int, input().split()))

# dp[i][j]: i번째 추까지 사용하여 추의 무게를 j로 만들 수 있는지 여부
dp = [[False] * 40001 for _ in range(n + 1)]

# 초기값 설정
dp[0][0] = True

# dp 계산
for i in range(1, n + 1):
    for j in range(40001):
        if dp[i - 1][j]:
            dp[i][j] = True
            if j + weights[i - 1] <= 40000:
                dp[i][j + weights[i - 1]] = True
            if abs(j - weights[i - 1]) <= 40000:
                dp[i][abs(j - weights[i - 1])] = True

# 결과 출력
for ball in balls:
    if dp[n][ball]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
        
'''
dp 생성 시 40,000개+1 로 생성하는 것이 중요 point!!
추 무게 += 구슬의 무게를 진행할 때 구슬의 무게가 최대 40,000이기에 이걸 고려해줘야한다! 안 한다면 indexError에 갇히게 될 것이야....
흔히 할 수 있는 실수: 15001개로 생성
--> 추 최대 갯수 30개 * 추 1개 최대 무게 500 = 15,000 이기에 발생하는 문제! 만약 추 무게 += 구슬의 무게 == 20,000대 혹은 30,000 대라면...?
'''