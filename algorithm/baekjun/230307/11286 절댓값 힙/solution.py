import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
import heapq

# heapq 를 사용한다면 가장 정석인 코드
hq = []
N = int(input())

for i in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])

# 통과하지만 효율적이지 못한 코드
'''
n = int(input())
heap = []
heap_abs = []
for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, a)
        heapq.heappush(heap_abs, abs(a))
    else:
        if not heap:
            print(0)
        else:
            min_val = heapq.heappop(heap_abs)
            if -min_val in  heap:
                print(-min_val)
                heap.remove(-min_val)
            else:
                print(min_val)
                heap.remove(min_val)
'''
            

# 시간 초과 나는 코드
'''
n = int(input())
heap = []
idx = 0
for _ in range(n):
    a = int(input())
    if a != 0:
        heap.append(a)
    else:
        if len(heap) == 0:
            print('0')
        elif len(heap) == 1:
            ans = heap.pop(0)
            print(ans)
        else:
            for i in range(len(heap)):
                if abs(heap[idx]) > abs(heap[i]):
                    idx = i
                elif abs(heap[idx]) == abs(heap[i]):
                    if heap[idx] > heap[i]:
                        idx = i
            ans = heap.pop(idx)
            print(ans)
            idx = 0
'''


'''
가장 정석적으로 문제 푸는 법을 떠올리지 못해 아쉬운 문제.
heap을 push할 때 한 값이 아닌 두 값의 묶음으로 push가 가능하다는 것을 알고 있었다면 좋았겠지만 그러지 못하여 떠올리지 못함
그래도 답이 나오게 하긴 했으니...절반의 성공이랄까
'''