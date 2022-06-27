import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def five(n, cnt):
    
    if n % 5 != 0:
        return cnt
    n = n // 5
    return five(n, cnt+1)

N = int(input())
five_cnt = 0
for i in range(1, N+1):
    five_cnt += five(i,0)

print(five_cnt)

# 끝자리 0 갯수는 결국 10이 몇 개 들었나 보는 것!
# 10 = 2 * 5인데 2가 5보다 무조건 많거나 같으므로 5 갯수만 파악해도 무방!