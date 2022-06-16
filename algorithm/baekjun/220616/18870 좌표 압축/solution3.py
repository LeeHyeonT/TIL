import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
nums = list(map(int, input().split()))

num_sort = sorted(list(set(nums)))
num_dict = dict()
for i in range(len(num_sort)):
    num_dict[num_sort[i]] = i

for j in nums:
    print(num_dict[j], end = ' ')

# 딕셔너리 조회는 시간복잡도가 O(1) 이라 통과할 수 있다!