import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, sys.stdin.readline().split())
num_lists = list(map(int, sys.stdin.readline().split()))
'''
미리 합을 구해놓고 꺼내쓰는 부분합을 사용했으나
일단은 시간초과....
input을 sys.stdin.readline 로 바꿔보자
---> 된다...!
이렇게 바꿔서 하는 것 고려해봐야겠다.....
'''
sum_lists = []
sum = 0
for num in num_lists:
    sum += num
    sum_lists.append(sum)

for tc in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result = sum_lists[j-1] - sum_lists[i-1] + num_lists[i-1]
    print(result)

# '''
# 이것도 결과론적으론 아래와 같은 로직인 것이니...
# 반복을 두 번 돌게해서는 안 된다
# '''

# def RegionalSum(end):
#     number = 0
#     index = 0
#     while True:
#         if index + 1 == end:
#             return number
#         number += num_lists[index]
#         index += 1


# for tc in range(M):
#     i, j = map(int, sys.stdin.readline().split())
#     if i == j:
#         result = num_lists[i-1]
#     else:
#         result = RegionalSum(j) - RegionalSum(i) + num_lists[j-1]
#     print(result)

# '''
# slicing보다 이게 과연 빠를까?
# 결과는 역시나 시간초과...!
# '''
# for tc in range(M):
#     i, j = map(int, input().split())
#     result = 0
#     for k in range(i-1, j):
#         result += num_lists[k]
#     print(result)

# '''
# 틀린 방법은 아니지만 시간초과 나오는 방법
# (시간초과 나오면 틀린 방법이라고 하는 게 맞나...?)
# '''
# for tc in range(M):
#     i, j = map(int, input().split())
#     result = sum(num_lists[i-1:j])
#     print(result)

# '''
# 전체에서 나머지 부분을 빼는 방법으로 해보자
# 역시나 시간초과다!
# '''
# for tc in range(M):
#     i, j = map(int, input().split())
#     result = sum(num_lists) - sum(num_lists[0:i-1]) - sum(num_lists[j:N])
#     print(result)
