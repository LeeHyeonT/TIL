input_dps = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"

lst = list(map(int, input_dps.split(", ")))
# index 그대로 계산하기 위해 7개가 아닌 8개씩 생성
grid = [[0]*8 for _ in range(8)]

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]
    grid[a][b] = 1
    grid[b][a] = 1

from pprint import pprint

pprint(grid)

stack = [1]
visited = [1]
while stack:
    tmp = stack[-1]

    for i in range(1, 8):

        if grid[tmp][i] == 1 and i not in visited:
            stack.append(i)
            visited.append(i)
            break
    else:
        stack.pop()

print(visited)