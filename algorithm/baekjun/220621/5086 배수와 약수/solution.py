import sys
sys.stdin = open('input.txt', encoding='UTF-8')

while True:
    m , n = map(int, input().split())
    if m == 0 and n == 0:
        break

    if n % m == 0:
        print('factor')
    elif m % n  == 0:
        print('multiple')
    else:
        print('neither')