import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

# N, C = map(int, input().split())

# houses = []
# for _ in range(N):
#     houses.append(int(input().rstrip()))

# houses.sort()
# start = houses[0]
# end = houses[-1]
# cnt = 1
# answer = 500000001
# while True:
#     if C == 2:
#         print(end - start)
#         break
#     else:
#         if cnt == C:
#             print(answer)
#             break
#         a = houses[int((cnt / (C-1)) * (len(houses)-1))]
#         if answer > a - houses[int(((cnt-1) / (C-1)) * (len(houses)-1))]:
#             answer =  a - houses[int(((cnt-1) / (C-1)) * (len(houses)-1))]
        
    
#     cnt += 1

import sys

n, c = map(int, sys.stdin.readline().split())
houses = []
for i in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()

start, end = 1, houses[-1]-houses[0]

result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 1  # 첫번째 집에는 무조건 공유기를 설치한다고 가정합니다.
    prev_house = houses[0]
    for i in range(1, n):
        if houses[i] - prev_house >= mid:
            cnt += 1
            prev_house = houses[i]
    if cnt >= c:  # 공유기의 개수를 줄입니다.
        start = mid + 1
        result = mid
    else:  # 공유기의 개수를 늘립니다.
        end = mid - 1
print(result)


'''
mid 를 그냥 거리라고 생각하고 하면 되는 문제
괜히 존재하는 집들 사이의 거리를 직접 구하고 다니면 안 되는 문제였다...!
시작 전 sort 를 실행해주는 것도 포인트
(최대 300,000개 이기에 sort 를 실행해도 시간이 초과되지 않음)
'''