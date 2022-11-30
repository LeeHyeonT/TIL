from itertools import combinations
import sys
sys.stdin = open('input.txt', encoding="UTF-8")

N = int(input())


num_list = [list(map(int, input().split())) for _ in range(N)]
num_list_reverse = num_list[::-1]
# print(num_list_reverse)

result = 0
# 세 자리 합의 일의 자리 숫자가 0일 수도 있으니 기본값 -1로 설정
result_point = -1
# num: 번호
for num in range(len(num_list_reverse)):
    combs = list(combinations(num_list_reverse[num], 3))
    point = 0
    for comb in combs:
        if sum(comb) % 10 == 9:
            point = sum(comb) % 10
            result = len(num_list_reverse) - num
            break
        elif sum(comb) % 10 > point:
            point = sum(comb) % 10

    if point == 9:
        break
    elif result_point < point:
        result_point = point
        result = len(num_list_reverse) - num
print(result)
'''
# 뒤부터 본다! 만약 맨 뒤에서 9 가 나온다면 이 놈이 무조건 승리한다!
하지만 이 방법이 전체를 다 도는 것보다 엄청 효율적이진 않은가보다...
'''
