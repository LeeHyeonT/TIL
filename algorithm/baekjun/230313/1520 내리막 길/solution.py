import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

'''
기본적인 dfs 를 이용한 코드. 시간 초과가 발생한다
'''
def dfs(x, y, array, visited):
    global cnt
    if x == m-1 and y == n-1:
        cnt += 1
        return
    for i in range(4):
        dx = x + delta[i][0]
        dy = y + delta[i][1]
        if ((0 <= dx < m) and (0 <= dy < n)) and (array[dx][dy] < array[x][y]) and visited[dx][dy] == 0:
            visited[dx][dy] = 1
            x = dx
            y = dy
            dfs(x, y, num_array, visited)
            visited[dx][dy] = 0
            x -= delta[i][0]
            y -= delta[i][1]

m, n = map(int, input().rstrip().split())
num_array = [list(map(int, input().rstrip().split())) for _ in range(m)]
visited = [[0]* n for _ in range(m)]
visited[0][0] = 1
delta = [[1,0], [0,1], [-1,0], [0,-1]]
x, y = 0, 0
cnt = 0
dfs(x, y, num_array, visited)
print(cnt)