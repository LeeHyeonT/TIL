import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
heights = [list(map(int, input().rstrip().split())) for _ in range(m)]

# dp 테이블 초기화
dp = [[-1] * n for _ in range(m)]

# dfs 함수 정의
def dfs(x, y):
    # 목적지에 도달한 경우 1 반환
    if x == m-1 and y == n-1:
        return 1
    
    # 이미 계산한 적 있는 경우 그 값을 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 계산한 적 없는 경우, 상하좌우 탐색
    dp[x][y] = 0
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] < heights[x][y]:
            dp[x][y] += dfs(nx, ny)
            
    return dp[x][y]

# 시작점부터 dfs 탐색 시작
print(dfs(0, 0))

'''
dp 초기화를 -1로 하는 것이 key point!
현재 값의 계산에 돌입할 때 해당 index 값을 0 으로 바꾸고 계산하기때문에 초기화를 0이 아닌 -1로 진행하는 것이다!
만약 초기화를 0으로 진행하고 비슷하게 코드를 진행해나간다면 모든 코드가 0으로 진행되기에 모든 부분을 다 반복하는 과정을 거쳐 시간 초과가 발생한다!!!
'''