import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
pattern1 = [['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B']]

pattern2 = [['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W']]

min_count = 10000
for i in range(M-8+1):
    for j in range(N-8+1):
        count1 = 0
        count2 = 0
        for k in range(8):
            for l in range(8):
                if arr[j+k][i+l] != pattern1[k][l]:
                    count1 += 1
        for k in range(8):
            for l in range(8):
                if arr[j+k][i+l] != pattern2[k][l]:
                    count2 += 1
        
        if count1 < min_count or count2 < min_count:
            if count1 < count2:
                min_count = count1
            else:
                min_count = count2

print(min_count)

# 이걸로 성공!
# 진짜 원초적인 방법이라 앞에 두 방법이 안 된 이유를 좀 더 생가해봐야 할 듯