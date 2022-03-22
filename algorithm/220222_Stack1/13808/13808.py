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
            
# 1. test case 입력받음
T = int(input())
# 2. 입력받은 test case 만큼 반복
for tc in range(1, T + 1):
    # 노드 갯수, 선 갯수 받아옴
    V, E = map(int, input().split())
    # 연결관계 저장할 dictionary 생성
    my_dic = {}
    # key 값을 노드값으로 해주고 value 를 list 의 형태로 빈 list 로 저장
    for i in range(1, V + 1):
        my_dic[i] = []
    # 연결관계 받아옴
    for _ in range(E):
        a, b = map(int, input().split())
        # a 가 기준 node(key), b 가 향할 node(value) 이므로 a를 key, b를 value 로 저장
        my_dic[a].append(b)
    # 시작, 끝값 받아옴
    start, end = map(int, input().split())
    # 함수에서 쓸 visited list 를 생성, start 값을 초기값으로 가짐
    visited = [start]
    # dfs 함수 실행
    dfs(start)

    # visited 안에 end 값이 있다면 start 지점에서 갈 수 있는것이므로 1, 아니라면 0 출력
    if end in visited:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")


