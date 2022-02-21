

# 처음부터 시작
for num in range(10):
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    # 우, 하, 좌 이동 델타값
    dx = [1, 0, -1]
    dy = [0, 1, 0]
    x = 0
    y = 0
    while x == 99:
        
        if arr[x][y] == 0:
            y += 1
        # 오른쪽으로 꺾는 과정: 0 나오기 전까지 진행
        if arr[x][y+1] == 1 and y+1 < 100:
            while arr[x][y+1] == 0:
                y += 1
        # 아래로 내려가는 과정: 교차로 나오기 전까지 진행
        if arr[x+1][y] == 1:
            while arr[x][y+1] == 1 or arr[x][y-1] == 1:
                x += 1


        # 답 나오는 경우
        if arr[x][y] == 2:
            ans_x = y
            break