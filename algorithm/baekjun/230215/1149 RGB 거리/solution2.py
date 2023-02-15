import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
house_paint = []
for _ in range(N):
    house_paint.append(list(map(int, input().rstrip().split())))

def Painting(idx):
    if idx >= N:
        return 
    house_paint[idx][0] += min(house_paint[idx-1][1], house_paint[idx-1][2])
    house_paint[idx][1] += min(house_paint[idx-1][0], house_paint[idx-1][2])
    house_paint[idx][2] += min(house_paint[idx-1][0], house_paint[idx-1][1])
    Painting(idx+1)

Painting(1)
print(min(house_paint[N-1][0], house_paint[N-1][1], house_paint[N-1][2]))


'''
위의 방법으로 진행하면 recursionError 가 발생한다.
1000번 이상 함수를 발동시키기 때문!
고로 for 문으로 진행시켜주어야 한다.
'''