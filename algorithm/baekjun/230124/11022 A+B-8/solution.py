import sys
sys.stdin = open('input.txt', encoding='uTF-8')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{tc}: {A} + {B} = {A+B}')

'''
안 틀리고 한 번에 맞아서 다행
예쁜 모양으로 출력하는 것 연습하는 문제
'''