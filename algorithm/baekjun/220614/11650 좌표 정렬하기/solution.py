import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
nums_lst = []
for _ in range(N):
    nums = list(map(int, input().split()))
    nums_lst.append(nums)


nums_lst.sort()
for i in nums_lst:
    for j in i:
        print(j, end=' ')
    print(end='\n')

# 다른 분들과 비교해보니 좋은 풀이는 아닌 것 같음
# 아래에 print 하는 과정에서 많은 시간을 소요하는 듯함