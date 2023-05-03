import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 무난한 풀이법
ans = 0
sum = 0
for _ in range(3):
    a, b = map(int, input().split())
    sum += b-a
    if sum > ans:
        ans = sum
print(ans)

# 그 때 그 때 승객수 파악
storage = []
sum = 0
for _ in range(4):
    a, b = map(int, input().split())
    sum += b-a
    storage.append(sum)

print(max(storage))