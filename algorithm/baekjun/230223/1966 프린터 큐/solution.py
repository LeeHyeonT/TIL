import sys
sys.stdin = open('input.txt', encoding='UTF-8')
import heapq

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    cnt = 0
    while True:
        if len(q) == 0:
            break
        
        if q[0] >= max(q):
            if m == 0:
                cnt += 1
                break
            else:
                q.pop(0)
                
                cnt += 1
                m -= 1
        else:
            if m == 0:
                a = q.pop(0)
                
                q.append(a)
                m = len(q) - 1
                
            else:
                a = q.pop(0)
                
                q.append(a)
                m -= 1
    
    print(cnt)


'''
heapq 는 이진 트리 형태라 사용할 때 주의가 필요하다
이 문제에서 heapq 의 heappop 을 시용한다면 array 내부의 숫자 배열이 바뀍게 되어
문제를 풀 수 없게 된다. 이 점 유의할 것
'''