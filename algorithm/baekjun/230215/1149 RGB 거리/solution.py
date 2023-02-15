import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
house_paint = []
for _ in range(N):
    house_paint.append(list(map(int, input().rstrip().split())))

start_list = [min(house_paint[0][0] + house_paint[1][1], house_paint[0][0] + house_paint[1][2]), 
min(house_paint[0][1] + house_paint[1][0], house_paint[0][1] + house_paint[1][2]), 
min(house_paint[0][2] + house_paint[1][0], house_paint[0][2] + house_paint[1][1])]
start = start_list.index(min(start_list))
charge = house_paint[0][start]
# charge = 0
def Painting(idx, color_idx):
    global charge
    if idx >= N:
        return 
    if idx < N-1:
        if (house_paint[idx][(color_idx+1)%3] + min(house_paint[idx+1][(color_idx+2)%3], house_paint[idx+1][(color_idx+3)%3])
            <= house_paint[idx][(color_idx+2)%3] + min(house_paint[idx+1][(color_idx+3)%3], house_paint[idx+1][(color_idx+4)%3])) :
            charge += house_paint[idx][(color_idx+1)%3]
            # print(idx, charge)
            Painting(idx+1, (color_idx+1)%3)
        elif (house_paint[idx][(color_idx+1)%3] + min(house_paint[idx+1][(color_idx+2)%3], house_paint[idx+1][(color_idx+3)%3])
            > house_paint[idx][(color_idx+2)%3] + min(house_paint[idx+1][(color_idx+3)%3], house_paint[idx+1][(color_idx+4)%3])) :
            charge += house_paint[idx][(color_idx+2)%3]
            # print(idx, charge)
            Painting(idx+1, (color_idx+2)%3)
    else:
        if house_paint[idx][(color_idx+1)%3] <= house_paint[idx][(color_idx+2)%3]:
            charge += house_paint[idx][(color_idx+1)%3]
            # print(idx, charge)
            Painting(idx+1, (color_idx+1)%3)
        elif house_paint[idx][(color_idx+1)%3] > house_paint[idx][(color_idx+2)%3]:
            charge += house_paint[idx][(color_idx+2)%3]
            # print(idx, charge)
            Painting(idx+1, (color_idx+2)%3)

Painting(1, start)
# Painting(0, 0)
print(charge)

'''
안타깝지만 맞추지 못함...
dp 의 개념은 전의 것으 보면서 전진하는 것인데 나는 이후의 것을 보며 전진해봄
그러니 문제가 잘 풀리지 않았다
고무적인 것은 개념 이해 자체는 잘 하고 있다는 것...? min으로 잘 표현하였다
'''