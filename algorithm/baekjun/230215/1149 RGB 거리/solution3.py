import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
house_paint = []
for _ in range(N):
    house_paint.append(list(map(int, input().rstrip().split())))

for i in range(1, N):
    house_paint[i][0] += min(house_paint[i-1][1], house_paint[i-1][2])
    house_paint[i][1] += min(house_paint[i-1][0], house_paint[i-1][2])
    house_paint[i][2] += min(house_paint[i-1][0], house_paint[i-1][1])


print(min(house_paint[N-1][0], house_paint[N-1][1], house_paint[N-1][2]))

'''
올바른 코드
'''