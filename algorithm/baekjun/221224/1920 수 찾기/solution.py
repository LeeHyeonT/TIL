sys.stdin = open('input.txt', encoding='UTF-8')
import sys
input = sys.stdin.readline
'''
정답이지만 아주 좋지 않은 방법
시간도, 메모리도 아주 많이 쓴다!
'''
N = int(input())
N_array = list(map(int, input().split()))
M = int(input())
M_array = list(map(int, input().split()))

N_array.sort()
for i in M_array:
    if i in N_array:
        print(1)
    else:
        print(0)
