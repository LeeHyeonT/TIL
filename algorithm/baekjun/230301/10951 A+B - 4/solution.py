import sys
sys.stdin = open('input.txt', encoding='UTF-8')

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break

'''
EndOfFunction 오류가 나오면 어떻게 할 것인지에 대한 문제
'''