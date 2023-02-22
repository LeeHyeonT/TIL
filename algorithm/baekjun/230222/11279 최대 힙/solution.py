import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = -int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            max_val = heapq.heappop(heap)
            print(-max_val)
    else:
        heapq.heappush(heap, x)

'''
python 기본 라이브러리인 heapq 를 활용하여 문제를 풀 수 있다.
안 쓴다면 시간초과의 압박이....
'''