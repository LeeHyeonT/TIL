import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

sum_list = [0] * N
sum_list[0] = num_list[0]
for i in range(1, N):
    sum_list[i] = max(num_list[i], sum_list[i-1] + num_list[i])
print(max(sum_list))

'''
dp 개념을 진짜 오랜만에 보는 것 같다....
기준 생각을 잘 해야하는데 그냥 숫자 하나 하나를 기준으로
현재 숫자보다 전의 것들의 합과 현재 숫자를 비교하여 더 큰 것을 계속 선택해나가는 방식으로 진행
'''
