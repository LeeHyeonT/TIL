import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
N = int(input())
num_array = list(map(int, input().rstrip().split()))
dp_inc = []
dp_dec = []

# i가 기준이 될 것
for i in range(N):
    num_array_inc = num_array[0:i]
    num_array_dec = num_array[i:N]
    dp_inc.append([0] * i)
    dp_dec.append([0] * (N-i))
    if i >= 1:
        dp_inc[i][0] = 1
    dp_dec[i][0] = 1

    for j in range(1, i):
        for k in range(j):
            if num_array_inc[j] > num_array_inc[k] and dp_inc[i][j] < dp_inc[i][k]:
                dp_inc[i][j] = dp_inc[i][k]
        dp_inc[i][j] += 1
    
    for m in range(1, N-i):
        for n in range(m):
            if num_array_dec[m] < num_array_dec[n] and dp_dec[i][m] < dp_dec[i][n]:
                dp_dec[i][m] = dp_dec[i][n]
        dp_dec[i][m] += 1
        
dp_inc.append([0] * N)
dp_dec.append([])
dp_inc[N][0] = 1
for j in range(1, N):
    for k in range(j):
        if num_array[j] > num_array[k] and dp_inc[N][j] < dp_inc[N][k]:
            dp_inc[N][j] = dp_inc[N][k]
    dp_inc[N][j] += 1


print(dp_inc)
print('-----------------------')
print(dp_dec)    
max_len = 0
max_inc = 0
max_dec = 0
for x in range(0, N+1):
    if len(dp_inc[x]) == 0:
        max_inc = 0
        max_dec = max(dp_dec[x])
    elif len(dp_dec[x]) == 0:
        max_inc = max(dp_inc[x])
        max_dec = 0
    else:
        max_inc = max(dp_inc[x])
        max_dec = max(dp_dec[x])
    if max_len < max_inc + max_dec:
        max_len = max_inc + max_dec
        
cnt = 0
for y in range(N-1):
    if num_array[y] == num_array[y+1]:
       cnt += 1
if cnt == N-1:
    print(1)
else: 
    print(max_len)
    
    
    
'''
잘못된 코드
계속 edge case 를 고쳐나갔지만 41% 정도에서 번번히 틀림
못 고친 edge case: 
1 2 3 3 3 2 1 처럼
같은 크기의 숫자가 나오는 경우
'''