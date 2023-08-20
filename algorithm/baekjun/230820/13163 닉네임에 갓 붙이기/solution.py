import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
for _ in range(n):
    name_list = list(map(str, input().split()))
    # 방법 1
    name_list[0] = 'god'
    print(''.join(name_list))
    
    # 방법 2
    # print('god', end='')
    # print(''.join(name_list[1:]))
    
'''
시간 차이는 거의 없는 방법 두 가지이다.
'''