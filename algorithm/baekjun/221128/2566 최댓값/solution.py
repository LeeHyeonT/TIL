import sys
sys.stdin = open('input.txt', encoding='UTF-8')

arr = []
for _ in range(9):
    arr.append(input().split())

ground_num = 0
vertical = 0
horizon = 0
for i in range(9):
    for j in range(9):
        # 문제 설명이 부실하다! 만약 최댓값이 같다면 뒤의 것을 출력해야한다!
        if int(arr[i][j]) >= ground_num:
            ground_num = int(arr[i][j])
            # 0 부터 시작하니 +1
            vertical = i + 1
            horizon = j + 1

print(ground_num)
print(vertical, horizon)
