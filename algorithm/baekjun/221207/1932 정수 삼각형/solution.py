import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    num = list(map(int, input().split()))
    num_list.append(num)

dp_list = list([0] * N for _ in range(N))
dp_list[0][0] = num_list[0][0]
# 행
for i in range(1, N):
    # 열
    for j in range(i+1):
        if j == 0:
            dp_list[i][j] = dp_list[i-1][j] + num_list[i][j]
        elif j == i:
            dp_list[i][j] = dp_list[i-1][j-1] + num_list[i][j]
        else:
            dp_list[i][j] = max(dp_list[i-1][j] + num_list[i]
                                [j], dp_list[i-1][j-1] + num_list[i][j])
# print(dp_list)
print(max(dp_list[N-1]))
'''
2차원 dp 문제
생각을 좀만 더 하면 쉽게 풀었을수도...?
오늘은 시간이 너무 부족했다
'''
