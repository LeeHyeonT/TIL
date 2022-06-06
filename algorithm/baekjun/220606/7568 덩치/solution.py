import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
body_arr = []
for _ in range(1,N+1):
    b = list(map(int, input().split()))
    body_arr.append(b)

cnt_arr = []
for body in body_arr:
    cnt = 1
    for ref in body_arr:
        if body[0] < ref[0] and body[1] < ref[1]:
            cnt += 1
    cnt_arr.append(cnt)


for count in cnt_arr:
    print(count, end=' ')