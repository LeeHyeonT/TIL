import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')

from collections import defaultdict

T = int(input())
for tc in range(1, T+1):
    # 노드 갯수, 간선 갯수
    V, E = map(int, input().split())
    # 노드간 연결관계 담아 둘 dictionary 생성
    dic = defaultdict(list)
    # 노드간 연결관계 input 에서 받아와 list 에 일단 저장
    lst = []
    for _ in range(E):
        lst.append(list(map(int, input().split())))
    # 출발 노드, 도착 노드
    S, G = map(int, input().split())
    # 앞서 저장한 list 값 이용하여 dictionary 에 노드간 연결관계 담아 둠
    for i in range(len(lst)):
        dic[lst[i][0]].append(lst[i][1])
        dic[lst[i][1]].append(lst[i][0])

    stack = []
    visited2 = []
    stack.append(S)
    visited2.append(S)
    cnt = 0
    while stack:
        tmp = stack[-1]
        for node in dic[tmp]:
            if node not in visited2:
                stack.append(node)
                visited2.append(node)
                break
        else:
            stack.pop()

        # DPS 실시 도중 stack 에 도착 노드값 들어오면
        if stack[-1] == G:
            cnt = len(stack) - 1
            break

    print(f"#{tc} {cnt}")