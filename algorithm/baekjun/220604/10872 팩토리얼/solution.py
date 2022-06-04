import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def fac(n):
    global res
    if n == 0:
        return 1
    elif n == 1:
        return res
    
    res = res * n
    fac(n-1)



N = int(input())
res = 1
fac(N)

print(res)

# 10! 이라는 숫자는 생각보다 매우 크다
# 쉬운 재귀일지라도 변수 선언 등 실수하지 말아야 할 것을 실수하면 안 된다!