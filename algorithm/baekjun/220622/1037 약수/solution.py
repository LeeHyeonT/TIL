import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N_num = int(input())
yaksu_lst = list(map(int, input().split()))

if N_num == 1:
    print(yaksu_lst[0] ** 2)
else:
    yaksu_lst.sort()
    print(yaksu_lst[0] * yaksu_lst[-1])



# 실버로 단계 올라가면 브론즈 문제는 반영 안 되나 확인 차 풀어본 문제
# 확인 결과 아주 반영 잘 된다!