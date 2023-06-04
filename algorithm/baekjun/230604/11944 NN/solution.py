import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n , m = map(int, input().split())
n  = str(n)
ans = ''
while True:
    if len(ans) >= m or len(ans) >= int(n) * len(n):
        break
    ans += n
ans.rstrip()
print(ans[:m])

'''
정답률이 낮은 이유는 그 이유가 분명히 있다...
문제의 조건을 확실히 파악하도록 해야한다. 
n 이 m 보다 크다면 문제가 쉽지만 (그렇게만 조건을 세워서 틀림)
n 이 m 보다 작은 경우도 고려해야 한다!
'''