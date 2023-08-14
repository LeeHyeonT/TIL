import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

storage = list(map(int, input().rstrip().split()))
# 방법 1
# cnt = 0
# for num in storage:
#     if num > 0:
#         cnt += 1   
# print(cnt)

# 방법 2
# ans = list(filter(lambda x: x > 0, storage))
# print(len(ans))
