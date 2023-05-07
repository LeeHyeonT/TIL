import sys
sys.stdin = open('input.txt', encoding='UTF-8')

t = int(input())
for _ in range(t):
    storage = list(map(str, input().split()))
    for i in range(len(storage)):
        for j in range(len(storage[i])-1, -1, -1):
            print(storage[i][j], end='')
        print(' ', end='')
    print('')
    
'''
[::-1] 안 쓰면 이렇게 푸는 방법 존재
'''