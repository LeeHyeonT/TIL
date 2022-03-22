import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    ch = [0] * (N+1)
    ch_L = [0] * (N+1)
    ch_R = [0] * (N+1)
    
    # 리프 노드에 배정된 값 넣어줌
    for i in range(1, M+1):
        nod_num, num = map(int, input().split())
        ch[nod_num] = num

    # 노드 간 연결관계 넣어줌
    for k in range(1, N+1):
        if 2*k + 1 <= N:
            ch_L[k] = 2*k
            ch_R[k] = 2*k+1
        elif 2*k <= N:
            ch_L[k] = 2*k

    # 후위순회 정의
    def postorder(T):
        if T != 0:
            postorder(ch_L[T])
            postorder(ch_R[T])
            if 2*T+1 <= N:
                ch[T] = ch[2*T] + ch[2*T+1]
            elif 2*T <= N:
                ch[T] = ch[2*T]

    postorder(1)
    print(f"#{tc} {ch[L]}")