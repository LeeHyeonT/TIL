import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
nums = list(map(int, input().split()))

num_comp = []
for num1 in nums:
    count = 0
    num_set = set()
    for num2 in nums:
        if num1 > num2:
            if num2 not in num_set:
                num_set.add(num2)
                count += 1
            
    num_comp.append(count)

for comp in num_comp:
    print(comp, end=' ')

# 시간복잡도 O(n^2) 라 시간초과가 난다.
# 이 풀이로는 답을 도출할 수 없음