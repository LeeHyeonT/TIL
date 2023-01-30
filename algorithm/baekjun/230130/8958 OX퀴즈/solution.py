import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
for _ in range(1, N+1):
    ox_string = input()
    count = 0
    answer = 0
    for ox in ox_string:
        if ox == 'O':
            count += 1
            answer += count
        else:
            count = 0
    print(answer)

'''
누적합 문제처럼 풀 수도 있겠지만 이 수준에서는 단순 계산으로 가능
만약 문자열 길이가 엄청 길어진다면 memoization을 활용해야 할듯
'''