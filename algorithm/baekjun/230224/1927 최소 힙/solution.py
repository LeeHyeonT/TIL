import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

'''
내장함수인 heapq를 사용하면 쉽게 풀 수 있는 문제
다만 tree 구조를 직접 만들어 사용할 줄도 알아야 나중에 나오는 더 어려운 문제를 이겨낼 수 있을 것
'''