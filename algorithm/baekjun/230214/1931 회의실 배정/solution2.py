import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
time_table = []
for _ in range(N):
    a = tuple(map(int, input().split()))
    time_table.append(a)

time_table.sort()
time_table.sort(key=lambda a : a[1])
visited = [False] * N
max_cnt = 0
cnt = 0
def MeetingTable(idx, past_idx):
    global max_cnt, cnt
    if idx >= N:
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    for i in range(idx, N):
        if cnt == 0:
            visited[i] = True
            cnt += 1
            if i+1 < N and time_table[i][0] == time_table[i+1][0]:
                MeetingTable(i+2, i)
                visited[i] = False
                cnt -= 1
            else:
                MeetingTable(i+1, i)
                visited[i] = False
                cnt -= 1
        elif time_table[i][0] >= time_table[past_idx][1] and not visited[i]:
            visited[i] = True
            cnt += 1
            if i+1 < N and time_table[i][0] == time_table[i+1][0]:
                MeetingTable(i+2, i)
                visited[i] = False
                cnt -= 1
            else:
                MeetingTable(i+1, i)
                visited[i] = False
                cnt -= 1

MeetingTable(0, 0)
print(time_table)
print(max_cnt)

'''
로직 양간 수정하고 약간의 성능 개선을 했지만 여전히 시간 초과...
'''