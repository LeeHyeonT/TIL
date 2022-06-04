import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def hanoii(n, start, mid, end):
    if n == 1:
        print(f'{start} {end}')
    else:
        hanoii(n-1, start, end, mid)
        print(f'{start} {end}')
        hanoii(n-1, mid, start, end)
N = int(input())
count = 2** N - 1
print(count)
hanoii(N, '1', '2', '3')

# 하노이 탑을 재귀로 푸는 것... 재귀의 알파이자 오메가라고 볼 수 있다.
# 눈으로 따라갈 때 헷갈리지 않을 때까지 보고 또 봐야할 것이다.