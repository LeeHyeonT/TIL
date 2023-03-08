import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

sum = 0
sums = []
for i in range(len(nums)):
    sum += nums[i]
    sums.append(sum)


mod_sums = []
cnt_mod_sums = [0] * m  # 0 ~ m-1 까지의 나머지 갯수를 저장하기 위한 list
for j in range(len(sums)):
    mod_sums.append(sums[j] % m)

for k in range(len(mod_sums)):
    cnt_mod_sums[mod_sums[k]] += 1

ans = cnt_mod_sums[0] # 0은 일단 만족하므로 더해놓고 시작
for cnt in cnt_mod_sums:
    if cnt != 0:
        ans += (cnt * (cnt-1)) // 2

print(ans)


'''
누적합 문제인데 아이디어가 필요했다
최소한의 반복으로 어떻게 답을 도출해낼지에 대한 아이디어...
답은 누적 합 자체의 나머지를 구하여 그걸로 이러쿵 저러쿵 하는 것이었다
같은 나머지가 몇 개 나왔는지 저장 후 그것을 조합(combination) 을 활용하여 푸는 문제.
'''