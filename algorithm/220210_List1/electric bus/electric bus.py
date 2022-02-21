import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(T):
    K, M, N = input().split()
    K = int(K)
    M = int(M)
    N = int(M)
    station_num = list(map(int, input().split()))
    cnt = [0]*(N+1)

    if K >= N:
        total_station_cnt = 0
        print(f"#{num + 1} {total_station_cnt}")
        continue

    for i in range(len(station_num)):
        cnt[station_num[i]] += 1

    total_station_cnt = 0
    for j in range(1, N//K + 1):
        station_cnt = 0
        # 아래에 있는 거 수정해야함, 인접한 station_num[i] 의 차가 K 이상이면
        # total_station_cnt = 0 g하고 break 하는 방향으로!
        for m in range(K*j - K + 1, K*j + 1):
            station_cnt += cnt[m]
            if station_cnt == 1:
                break

        if station_cnt == 0:
            total_station_cnt = 0
            break

        total_station_cnt += station_cnt

    print(f"#{num+1} {total_station_cnt}")