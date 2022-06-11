import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
num_arr = []

for _ in range(N):
    num = int(input())
    num_arr.append(num)

count = [0] * (len(num_arr) + 1)
for num in num_arr:
    count[num] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0]* len(num_arr)

for num in num_arr:
    idx = count[num]
    result[idx -1] = num
    count[num] -= 1

for a in result:
    print(a)


# 이 방법으로는 못 푼다! 
# 이 방법은 음수를 지원하지 않기 때문!