import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
time_table = []
for _ in range(N):
    a = tuple(map(int, input().split()))
    time_table.append(a)

time_table.sort()
visited = [False] * N
max_cnt = 0
cnt = 0
def MeetingTable(idx, past_idx):
    global max_cnt, cnt
    if idx >= N-1:
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    for i in range(idx, N):
        if idx == past_idx:
            visited[i] = True
            cnt += 1
            MeetingTable(i+1, i)
            visited[i] = False
            cnt -= 1
        elif time_table[i][0] >= time_table[past_idx][1] and not visited[i]:
            visited[i] = True
            cnt += 1
            MeetingTable(i+1, i)
            visited[i] = False
            cnt -= 1

MeetingTable(0, 0)
print(max_cnt)

'''
로직은 맞지만 모든 부분을 다 돌아보기에 시간초과가 나는 코드...
+ 다시보니 로직도 뭔가 이상한 부분이 있다.
'''
