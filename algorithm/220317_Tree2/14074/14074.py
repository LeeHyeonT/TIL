import sys
sys.stdin = open("input.txt", "r")

# 최소 heap 하는 과정
def lowerheap(n):
    idx = 1
    while True:
        # 문제에서 값이 하나하나 들어온다고 했으므로 하나하나 넣어줌
        heap_list.append(ch[idx])
        # 0번 index 포함하여 heap_list 길이 3 이상이어야 자리바꿈 가능
        if len(heap_list) >= 3:
            # 뒤에서부터 진행: // 값 활용하기 위하여
            for i in range(len(heap_list)-1, 0, -1):
                if heap_list[i//2] and heap_list[i//2] > heap_list[i]:
                    heap_list[i//2], heap_list[i] = heap_list[i], heap_list[i//2]

        idx += 1
        if idx > n:
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ch = [0] + list(map(int, input().split()))
    heap_list = [0]
    lowerheap(N)

    parent_sum = 0
    while N >= 1:
        N = N//2
        parent_sum += heap_list[N]

    print(f"#{tc} {parent_sum}")

