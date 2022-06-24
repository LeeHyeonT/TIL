import sys
sys.stdin = open('input.txt', encoding='UTF-8')

from itertools import combinations
N, K = map(int, input().split())
lst_1 = []

for i in range(N):
    lst_1.append(i)
b = list(combinations(lst_1, K))
print(len(b))
# 오랜만에 combinations 라이브러리 사용
# 이 방법은 좋긴 하지만...아래 방법이 시간이 초과된 이유를 살펴보자

tmp1 = N - K

num1 = 1
num2 = 1

while True:
    if tmp1 == 1:
        break
    num1 = num1 * N
    tmp1 -= 1
    N -= 1

while True:
    if K == 1:
        break
    num2 = num2 * K
    K -= 1

print(round(num1 / num2))

# 시간복잡도 자체는 O(N) 으로 나쁘지 않은데 1초 안에 들어오진 못한다...
# N, K값 범위도 10까진데 왜 못 들어오는건지 잘 모르겠다...