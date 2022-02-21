import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 몇 번 입력할 지 받음
T = int(input())
# test case 입력받은 만큼 반복
for tc in range(1, T+1):
    # 받아온 (, ) 들 하나하나 list 의 요소로 만들어줌
    lst = list(map(str, input()))
    # 현재 사용중인 파이프 세는 것은 cnt, 쪼개진 총 파이프 갯수는 sol
    cnt = sol = 0
    for i in range(len(lst)):
        # 파이프가 하나 생성되었으므로 count 1 올려줌
        if lst[i] == "(":
            cnt += 1
        # 파이프가 끝나는 경우 / 레이저가 만들어지는 경우 로 나눠서 생각
        elif lst[i] == ")":
            # 레이저가 만들어진다면 현재 count 된 파이프들이 쪼개지면서 sol 값에 더해줌
            # 앞의 ( 에서 count 를 1 올려줬기 때문에 count 먼저 1 빼주고 진행
            if lst[i-1] == "(":
                cnt -= 1
                sol += cnt
            # 파이프가 끝난 경우에는 sol 값에 1이 추가되면서 count 하나 줄음
            else:
                sol += 1
                cnt -= 1
                
    print(f"#{tc} {sol}")

