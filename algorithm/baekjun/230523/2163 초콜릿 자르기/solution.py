import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, m = map(int, input().split())
if n == 1 and m == 1:
    print(0)
elif n == 1:
    print(m-1)
elif m == 1:
    print(n-1)
else:
    print(min(n-1 + (m-1)*n, m-1 + (n-1)*m))
    

'''
먼저 한 방향으로 잘라놓고 생각하는 문제.
'''
    