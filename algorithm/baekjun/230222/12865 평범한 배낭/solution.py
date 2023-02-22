import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
WV = []
for _ in range(N):
    WV.append(list(map(int, input().rstrip().split())))

cnt = 0
weight = 0
max_weight = 0
def Function(array, idx):
    global cnt, weight, max_weight
    if cnt > K:
        return
    else:
        if max_weight < weight:
            max_weight = weight
    
    for i in range(idx, len(array)):
        cnt += array[i][0]
        weight += array[i][1]
        Function(array, idx+1)
        cnt -= array[i][0]
        weight -= array[i][1]

Function(WV, 0)
print(max_weight)

'''
dynamic programming 문제라 dfs/bfs 를 사용하면 시간 초과가 나온다...!
'''
         