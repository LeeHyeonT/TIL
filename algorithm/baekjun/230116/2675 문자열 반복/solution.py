import sys
sys.stdin = open("input.txt", encoding='UTF-8')

T = int(input())
for _ in range(T):
    N, string = map(str, input().split())
    answer = ''
    for i in range(len(string)):
        answer = answer + string[i] * int(N) 
    print(answer)