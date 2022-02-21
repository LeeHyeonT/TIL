import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 갯수 받아옴
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    # 버스 노선 갯수 받아옴
    N = int(input())
    # 버스 노선은 시작, 끝만 존재하기에 그 두 값을 묶어서 list 로 저장하기 위해 list 생성 
    bus_lst = []
    for bus in range(N):
        bus_lst.append(list(map(int, input().split())))
    # 버스정류장도 따로 저장해놓기 위해 list 생성    
    bus_stop_lst = []
    # 버스정류장 갯수 받아옴
    P = int(input())
    for _ in range(P):
        bus_stop_lst.append(int(input()))
    # 버스 노선이 버스 정류장을 몇 번 지나느지 알기 위해 count 하는 list 생성
    # 노선이 오름차순으로 나와있으면 이 방법이 가능하지만 그게 아니라면 이렇게 하면 안 됨
    bus_stop_cnt = [0] * P
    # 버스정류장 갯수만큼 반복
    for i in range(len(bus_stop_lst)):
        # 그 안에서 버스 노선 갯수만큼 반복
        for j in range(len(bus_lst)):
            # 버스 노선의 두 숫자 사이에 버스정류장이 존재하면 count + 1 해줌
            if bus_lst[j][0] <= bus_stop_lst[i] <= bus_lst[j][1]:
                bus_stop_cnt[i] += 1

    print(f"#{tc}", *bus_stop_cnt)
