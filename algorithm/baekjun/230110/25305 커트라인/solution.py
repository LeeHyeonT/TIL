import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
N, K = map(int, input().split())
score_list = [0] + list(map(int, input().split()))

score_list.sort()
print(score_list[N-K+1])

'''
0을 하나 더 넣고 숫자 그대로 쓰는 게 포인트
만약 0을 안 넣었으면 N-K 만 해도 됨
'''