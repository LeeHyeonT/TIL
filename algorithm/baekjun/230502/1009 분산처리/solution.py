import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    a, b = map(int, input().split())
    mod_a = a % 10
    mod_b = b % 4 if b % 4 != 0 else 4
    result = mod_a ** mod_b % 10
    if result == 0:
        result = 10
    print(result)
    

'''
4번마다 반복된다는 규칙을 깨달으면 쉬운 문제
'''