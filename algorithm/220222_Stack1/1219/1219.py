import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


# dfs 함수 생성
def dfs(start):
    # node 값을 현재 my_dic 안의 start key 의 value 값으로 설정
    for node in my_dic[start]:
        # visited 안에 node 값이 없다면 그 값을 visited 에 더해주고 dfs 함수 재귀실행
        if node not in visited:
            visited.append(node)
            dfs(node)


for _ in range(10):
    tc, L = map(int, input().split())
    # 연결관계 저장할 dictionary 생성
    my_dic = {}
    # key 값을 0~99 로 해주고 value 를 list 의 형태로 빈 list 로 저장
    for i in range(100):
        my_dic[i] = []
    # node 쌍들을 받아옴
    way = list(map(int, input().split()))
    # 2개씩 짤라서 각각 읽어 my_dic 의 key, value 로 사용
    for i in range(0, len(way), 2):
        a = way[i]
        b = way[i + 1]
        my_dic[a].append(b)

    visited = [0]
    dfs(0)

    # visited 안에 end 값이 있다면 start 지점에서 갈 수 있는것이므로 1, 아니라면 0 출력
    if 99 in visited:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
