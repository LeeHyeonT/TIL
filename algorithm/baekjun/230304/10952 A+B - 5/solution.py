import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

while True:
    A, B = map(int, input().rstrip().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)