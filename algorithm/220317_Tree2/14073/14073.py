import sys
sys.stdin = open("input.txt", "r")

# 중위순회 정의
def inorder(T):
    global i
    if T != 0:
        inorder(ch_L[T])
        cbs[T] = i
        i += 1
        inorder(ch_R[T])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ch_L = [0] * (N + 1)
    ch_R = [0] * (N + 1)

    # 노드 간 연결관계 넣어줌
    for k in range(1, N+1):
        if 2*k + 1 <= N:
            ch_L[k] = 2*k
            ch_R[k] = 2*k+1
        elif 2*k <= N:
            ch_L[k] = 2*k

    cbs = [0] * (N+1)
    # 노드 갯수: 1,2,3,4... / 값의 크기: 1,2,3,4...이므로 그냥 1부터 시작하여 1씩 더해주면 됨
    i = 1
    inorder(1)
    print(f"#{tc} {cbs[1]} {cbs[N//2]}")
