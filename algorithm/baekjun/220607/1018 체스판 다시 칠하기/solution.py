import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())

arr = [list((map(str, input().split()))) for _ in range(N)]

print(arr)
print(arr[0][0][0])
min_count = 1000
for i in range(M-8+1):
    for j in range(N-8+1):
        # i ~ i+7
        # j ~ j+7
        count = 0
        if arr[j][0][i] == 'W':
            for l1 in range(j, j+8, 2):
                for k1 in range(i, i+8, 2):
                    if arr[l1][0][k1] == 'B':
                        count += 1
                for k2 in range(i+1, i+9, 2):
                    if arr[l1][0][k2] == 'W':
                        count += 1
            for l2 in range(j+1, j+9, 2):
                for k1 in range(i, i+8, 2):
                    if arr[l2][0][k1] == 'W':
                        count += 1
                for k2 in range(i+1, i+9, 2):
                    if arr[l2][0][k2] == 'B':
                        count += 1
        else:
            for l1 in range(j, j+8, 2):
                for k1 in range(i, i+8, 2):
                    if arr[l1][0][k1] == 'W':
                        count += 1
                for k2 in range(i+1, i+8, 2):
                    if arr[l1][0][k2] == 'B':
                        count += 1
            for l2 in range(j+1, j+9, 2):
                for k1 in range(i, i+8, 2):
                    if arr[l2][0][k1] == 'B':
                        count += 1
                for k2 in range(i+1, i+8, 2):
                    if arr[l2][0][k2] == 'W':
                        count += 1

        if min_count > count:
            min_count = count
    
print(count)