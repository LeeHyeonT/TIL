import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')

from collections import defaultdict
from collections import deque
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

    # DPS 실시: 각 노드 번호로부터의 출발을 반복하는 과정
    for j in range(1, V+1):
        stack = []
        visited2 = []
        stack.append(j)
        visited2.append(j)
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

            # stack 에 아무것도 안 들어있으면 다음 노드 번호 DPS 실시
            if len(stack) == 0:
                break
            # DPS 실시 도중 stack 에 도착 노드값 들어오면
            elif stack[-1] == G:
                # 출발 노드값이 stack 에 들어있는지 살펴보고
                if S in stack:
                    # 있다면 index 활용하여 두 노드가 얼마나 떨어져있는지 구함
                    cnt = len(stack) - stack.index(S) - 1
                    break
        # 앞서 cnt 값을 구했다면 다음 노드 번호 DPS 는 실시할 필요가 없으므로 반복 빠져나옴
        if cnt != 0:
            break

    print(f"#{tc} {cnt}")


    # visited1 = []
    # q = deque()
    # cnt = 0
    # visited1.append(1)
    # q.append(1)
    #
    # while q:
    #     tmp = q.popleft()
    #     for node in dic[tmp]:
    #         if node not in visited1:
    #             q.append(node)
    #             visited1.append(node)
    #         print(visited1)