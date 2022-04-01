import sys
sys.stdin = open('input.txt', 'r')

# 이진탐색 구현 및 문제에 맞는 조건 넣기
def binarySearch(a, N, key):
    global cnt
    start = 0
    end = N-1
    # 문제에서 왼쪽 오른쪽 번갈아 보는 경우를 찾으라 해서 왼쪽으로 갈 때 사용할 값과 오른쪽으로 갈 때 사용할 값 생성
    cnt_left = 0
    cnt_right = 0
    
    # 주어진 숫자가 무조건 기준 안에 존재하는 건 아니므로 존재하지 않는다면 함수 종료
    if key not in a:
        return
    # 이진탐색 시작
    # 만약 한 쪽으로 두번 연속 간다면 (cnt_left, cnt_right) = (2,0) or (0,2) 이기에 조건을 저렇게 넣음
    while start <= end and not (abs(cnt_left - cnt_right) == 2):
        middle = (start + end) // 2
        if a[middle] == key:
            cnt += 1
            return
        elif a[middle] > key:
            end = middle - 1
            # 왼쪽으로 이동했으니 왼쪽값 +1 해주고 오른쪽값 리셋
            cnt_left += 1
            cnt_right = 0
        else:
            start = middle + 1
            # 오른쪽으로 이동했으니 오른쪽값 +1 해주고 왼쪽값 리셋
            cnt_right += 1
            cnt_left = 0

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for b in B:
        binarySearch(A, N, b)
    print(f"#{tc} {cnt}")