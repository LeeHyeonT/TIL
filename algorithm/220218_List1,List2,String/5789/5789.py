import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 몇 번 있는지 입력받음
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # 값 저장할 list 생성, index 그래도 받아올 것이므로 앞쪽에 0 하나 더 붙임
    lst = [0] * (N+1)
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            # 위의 i가 0부터 시작하는데 실제로 더해지는 값은 1부터이므로 i+1
            # 이렇게 안 하려면 위의 for 문을 for i in range(1,Q+1) 로 하면 됨
            lst[j] = i+1

    print(f"#{tc}", *lst[1:])