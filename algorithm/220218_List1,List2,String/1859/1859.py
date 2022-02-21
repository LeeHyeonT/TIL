import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 만큼 입력받음
T = int(input())
# text case 만틈 반복 진행
for tc in range(1, T+1):
    N = int(input())

    sol = 0
    lst = list(map(int, input().split()))
    # list 의 맨 뒤에서부터 접근, 일단 맨 뒤 list 요소를 max 값으로 잡아놓음
    max_lst = lst[-1]
    for j in range(len(lst)-2, -1, -1):
        # 현재 인덱스에 위치한 값이 max_lst 보다 작으면 둘의 차를 sol 에 더해줌
        if lst[j] < max_lst:
            sol += max_lst - lst[j]
        # 그게 아니라면 max_lst 값 교체
        else:
            max_lst = lst[j]

    print(f"#{tc} {sol}")