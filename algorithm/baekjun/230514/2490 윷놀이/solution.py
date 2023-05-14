import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(3):
    storage = list(map(int, input().split()))
    if sum(storage) == 1:
        print('C')
    elif sum(storage) == 2:
        print('B')
    elif sum(storage) == 3:
        print('A')
    elif sum(storage) == 4:
        print('E')
    else:
        print('D')    