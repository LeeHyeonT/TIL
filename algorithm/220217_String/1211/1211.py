import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

# 끝에서부터 시작
for num in range(10):
    case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dic = {"y": 0, "count": 10000}
    # 1인 지점에서만 진행하면 되므로 1이 아닌 경우 다음 i 로 넘어감
    for i in range(100):
        if arr[99][i] == 1:
            y = i
        else:
            continue
        # 지나온 부분에 0을 넣는 방식으로 진행하면 한 번밖에 진행할 수 없기 때문에
        # deepcopy 를 통해 복사본을 만들어 여기서 하나하나 진행할 예정
        arr_copy = [item[:] for item in arr]
        x = 99
        y = i
        cnt = 0

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
                    if arr_copy[nx][ny] == 1:
                        arr_copy[x][y] = 0
                        x = nx
                        y = ny
                        cnt += 1

        if cnt < dic['count']:
            dic['y'] = y
            dic['count'] = cnt

    print(f"#{num + 1} {dic['y']}")
