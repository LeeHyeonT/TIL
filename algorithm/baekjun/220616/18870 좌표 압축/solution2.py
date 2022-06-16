import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
nums = list(map(int, input().split()))

num_sort = sorted(list(set(nums)))


for i in nums:
    print(num_sort.index(i), end=' ')

# 이 방법도 O(n^2) 복잡도라 안 된다!