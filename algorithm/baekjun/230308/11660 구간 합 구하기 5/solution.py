import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

# 이게 python3 로 시간초과가 나네...? pypy로는 통과
'''
n, m = map(int, input().rstrip().split())
num_array = []
sum_array = [[0] * n for _ in range(n)]
for _ in range(n):
    num_array.append(list(map(int, input().rstrip().split())))

# 각 행에 대한 누적합 구하기
for i in range(n):
    s = 0
    for j in range(n):
        s += num_array[i][j]
        sum_array[i][j] = s

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    ans = 0
    for j in range(x1 - 1, x2): # 둘러봐야하는 행의 갯수: (y1-1) 행부터 (y2-1) 행까지
        if y1 == 1:
            ans += sum_array[j][y2 - 1]
        else:
            ans += sum_array[j][y2 - 1] - sum_array[j][y1 - 2]
    print(ans)
'''

# 하다가 마무리 못한 코드
'''
n, m = map(int, input().rstrip().split())
num_array = []
sum_heng = [[0] * n for _ in range(n)]
sum_yeol = [[0] * n for _ in range(n)]
for _ in range(n):
    num_array.append(list(map(int, input().rstrip().split())))

# 각 행에 대한 누적합 구하기
for i in range(n):
    s = 0
    for j in range(n):
        s += num_array[i][j]
        sum_heng[i][j] = s
# 각 열에 대한 누적합 구하기
for i in range(n):
    s = 0
    for j in range(n):
        s += num_array[j][i]
        sum_yeol[i][j] = s
print(sum_heng)
print(sum_yeol)
# ex) 누적 합의 2행 2열: 숫자 배열의 1행 1열부터 2행 2열까지의 합
sum_array = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        pass
    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    ans = 0
    for j in range(x1 - 1, x2): # 둘러봐야하는 행의 갯수: (y1-1) 행부터 (y2-1) 행까지
        pass
    print(ans)
'''


'''
행 누적합 따로, 열 누적합 따로 구해서 내가 원하는 방향의 누적합을 구하는 것이 아닌 (시간 초과의 위험)
처음 숫자 배열을 보고 내가 원하는 누적합을 구해서 진행하는 문제,
'''