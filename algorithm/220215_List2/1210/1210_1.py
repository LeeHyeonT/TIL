import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# 끝에서부터 시작
for num in range(10):
    case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(100):
        if arr[99][i] == 2:
            y = i
            break
    x = 99
    y = i

    # 우 좌 상 방향 결정
    dx = [0, 0, -1]
    dy = [1, -1, 0]
    # 맨 꼭대기에 도달할 때까지 진행: x값이 0이 될 때까지 진행!
    while x != 0:
        # 우, 좌, 상 방향 갈 수 있도록 새로운 x,y 값 만들어줌
        for j in range(3):
            nx = x + dx[j]
            ny = y + dy[j]
            # 새로운 x,y 값이 idx 를 벗어나지 않고 적용했을때의
            # arr 값이 1인 경우 전 부분을 지우고(0으로 만들고) x,y 변경
            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[nx][ny] == 1:
                    arr[x][y] = 0
                    x = nx
                    y = ny


    print(f"#{num+1} {y}")