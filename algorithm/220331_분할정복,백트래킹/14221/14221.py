import sys
sys.stdin = open('input.txt', 'r')

# 이 식 자체에서는 값 배분하는 건 없다. 배분하는 건 partition 할 때 진행
def quick_sort(lst, l, r):
    # print(lst)
    if l < r:
        pivot = hoare_partition(lst, l, r)
        quick_sort(lst, l, pivot-1)
        quick_sort(lst, pivot+1, r)


# 방식: i, j 는 인덱스, i는 왼쪽 끝 / j는 오른쪽 끝에서 출발
# i는 피봇 값보다 큰 값이 나올 때까지 증가, j는 피봇 값보다 작은 값이 나올 때까지 감소
# 위의 두 경우를 만족하는 경우를 찾으면 두 값을 서로 바꿔줌
# i>=j 인 상황이 오면 현재 pivot 과 j에 존재하는 값을 서로 바꿔줌
def hoare_partition(lst, l, r):
    pivot = lst[l]
    i = l
    j = r
    while i <= j:
        while i <= j and lst[i] <= pivot:
            # while not (lst[i] > pivot):
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    #이건 가능: lst[l], lst[j] = lst[j], pivot
    #이건 불가: pivot, lst[j] = lst[j], pivot

    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(nums, 0, N-1)
    print(f"#{tc} {nums[N//2]}")
