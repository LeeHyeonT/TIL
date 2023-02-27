import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())

for i in range(max(1, N - 9 * 17), N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)
    

'''
아이디어가 필요한 문제
생성자이 될 수 있는 가짓수가 그렇게 많지 않다는 것을 이용
각 자릿수의 최댓값은 9이니 N의 최대 자릿수  * 9 개의 수만 생성자가 될 수 있다
'''