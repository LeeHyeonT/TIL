import sys
sys.stdin = open('input.txt', encoding='UTF-8')
import heapq

a = [1,2,3,4]
print(a)
b = heapq.heappop(a)
c = heapq.heappop(a)
print(a)
a.append(b)
a.append(c)
print(b)
print(a)