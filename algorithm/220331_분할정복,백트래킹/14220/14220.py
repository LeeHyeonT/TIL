import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


# 최소 크기로 쪼개는 과정
def merge_sort(lst):
    # 최소 크기가 되면 쪼개기 종료
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2

    left = lst[:middle]
    right = lst[middle:]

    # recursive 하게 계속 쪼갬
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# 쪼갠 애들을 토대로 정렬하는 과정
def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1
    # 위의 cnt 값만 잘 구했으면 나머지 정렬은 일반적인 merge sort 보다 빠른 방법 택해도 괜찮음!
    result = left + right
    result.sort()
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    print(f"#{tc} {merge_sort(lst)[len(lst)//2]} {cnt}")