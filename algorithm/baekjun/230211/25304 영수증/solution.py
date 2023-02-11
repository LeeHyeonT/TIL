import sys
sys.stdin = open('input.txt', encoding='UTF-8')

X = input()
N = int(input())
total_price = 0
for _ in range(N):
    a, b = map(int, input().split())
    total_price += a * b

if len(X) != len(str(total_price)):
    print('No')
else:
    for i  in range(len(X)):
        if X[i] != str(total_price)[i]:
            print('No')
            break
    else:
        print('Yes')

'''
그냥 숫자끼리 비교해도 이 정도 크기는 빠르게 구할 수 있지만 더 큰 숫자일 때를 대비하여
str 끼리의 비교로 한 번 풀어봄
'''