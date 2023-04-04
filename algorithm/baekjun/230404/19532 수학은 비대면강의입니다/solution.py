import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a, b, c, d, e, f = map(int, input().split())
if a == 0:
    y = c/b
    x = (f - e*y)/d
    print(int(x), int(y))
else:
    y = (a*f - c*d) / (a*e - b*d)
    x = c/a - (b*y)/a
    print(int(x), int(y))

'''
수학문제
'''