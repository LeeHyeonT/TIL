import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
wires = []
for i in range(n):
    a, b = map(int, input().split())
    wires.append((a, b))

wires.sort()
dp = [1] * n    # 남아있을 수 있는 전선 갯수 표현하기 위한 dp

for i in range(n):
    for j in range(i):
        if wires[j][1] < wires[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(wires)
print(dp)
print(n - max(dp))  # 끊어야 할 전선 갯수를 보여줘야하기에 전체 - 최대로 남아있을 수 있는 전선 갯수로 표현

'''
sort 로 시작하는 것이 맞았다!
괜히 의심하지 말자....!
'''