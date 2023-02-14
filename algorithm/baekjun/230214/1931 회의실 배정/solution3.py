import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j
print(time)
print(conut)

'''
끝나는 시간 기준으로 정렬하는 것이 포인트였다....
생각해보니 끝나는 시간이 적어야 더 많은 회의를 개설하는 것이 맞기에 저런 정렬이 맞다!
끝나는 시간을 기준으로 정렬한다면 재귀함수를 사용할 이유도 사라진다...
'''