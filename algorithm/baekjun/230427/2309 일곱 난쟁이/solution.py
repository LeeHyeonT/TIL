import sys
sys.stdin = open('input.txt', encoding='UTF-8')
from itertools import combinations

nums = []
for _ in range(9):
    num = int(input())
    nums.append(num)

storage = combinations(nums,7)
for bundle in storage:
    if sum(bundle) == 100:
        ans = list(bundle)
        ans.sort()
        for i in ans:
            print(i)
        break


'''
break 을 잘 붙입시다...! 사소한 실수는 금물!
'''