N = int(input())
num_arr = []

for _ in range(N):
    num = int(input())
    num_arr.append(num)

num_arr.sort()

for a in num_arr:
    print(a)

# 내장되어있는 sort 방식이 퀵 소트 기반 NlogN 방식
# 이걸로도 100만 숫자정도는 2초 이내에 정렬 가능