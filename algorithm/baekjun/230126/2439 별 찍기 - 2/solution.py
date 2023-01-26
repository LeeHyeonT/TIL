import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
for i in range(1, N+1):
    print(' ' * (N-i), end='')
    print('*' * i)


'''
print(' ' * (N-i), '*' * i) 로 하면 답이 아니다!
처음 한 칸이 띄어진 채로 시작하기 때문!
'''