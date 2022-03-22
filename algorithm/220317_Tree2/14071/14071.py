import sys
sys.stdin = open("input.txt", "r")

# 아무 순회나 사용 가능: 여기선 그냥 전위순회
def preorder(T):
    global cnt
    if T != 0:
        cnt +=1
        preorder(ch_L[T])
        preorder(ch_R[T])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 노드 갯수보다 1개 더, 맨 앞의 index 위해 1개 더 하여 E+2 개 생성
    ch_L = [0] * (E+2)
    ch_R = [0] * (E+2)
    relation = [0] + list(map(int, input().split()))

    for i in range(1,len(relation), 2):
        if ch_L[relation[i]] == 0:
            ch_L[relation[i]] = relation[i+1]
        else:
            ch_R[relation[i]] = relation[i+1]

    # 기준 노드 넣어 아래 subtree 갯수 세기
    cnt = 0
    preorder(N)
    print(f"#{tc} {cnt}")
