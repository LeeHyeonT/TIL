import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())

arr = [list((map(str, input().split()))) for _ in range(N)]

print(arr)
min_count = 1000
pattern1 = 'WBWBWBWB'
pattern2 = 'BWBWBWBW'

for i in range(M-8+1):
    for j in range(N-8+1):
        # i ~ i+7
        # j ~ j+7
        count = 0
        if arr[j][0][i] == 'W':
            for l in range(j, j+8, 2):
                
                for k in range(8):
                    if arr[j][0][i+k] != pattern1[k]:
                        count += 1
                print(f'W시작1: 여기는 {count}')
            for l in range(j+1, j+9, 2):
                for k in range(8):
                    if arr[j][0][i+k] != pattern2[k]:
                        count += 1
                print(f'W시작2: 여기는 {count}')
        else:
            for l in range(j, j+8, 2):
              
                for k in range(8):
                    if arr[j][0][i+k] != pattern2[k]:
                        count += 1
                print(f'B시작1: 여기는 {count}')
            for l in range(j+1, j+9, 2):
                for k in range(8):
                    if arr[j][0][i+k] != pattern1[k]:
                        count += 1
                print(f'B시작2: 여기는 {count}')
           

        if min_count > count:
            min_count = count
    
print(count)
print(min_count)