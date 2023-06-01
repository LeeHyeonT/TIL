import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
case = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0:
        break
    else:
        a = v // p
        b = v % p
        if l > b:
            ans = a * l + b
        else:
            ans = a * l + l
        print(f'Case {case}: {ans}')
    
    case += 1
    
    
'''
실수하기 딱 좋은 문제(인 것 같으면서도 외부 요인 때문에 한 번 틀려버렸다)
어떠한 문제든지 조건을 명확히 파악해야한다!!
'''