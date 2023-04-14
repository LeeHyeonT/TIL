import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    age, name = map(str, input().rstrip().split())
    array.append([int(age), name])

array.sort(key=lambda x: x[0])
for ans in array:
    print(*ans)
    
'''
입력된 순서도 필요하기에 set() 을 활용할 수는 없다!
'''