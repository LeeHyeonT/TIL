

# 끝에서부터 시작
for num in range(10):
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    # 우, 하, 좌 이동 델타값
    dx = [1, 0, -1]
    dy = [0, 1, 0]
    x = 99
    y = 99
    while x == 0:
        ans_x = y


        if arr[x + 1][y] == 1:
            x += 1