import sys
sys.stdin = open('input.txt', encoding='UTF_8')

N, M = map(int, input().split())
standard_array = []
def Solution(N, M, start):
    if len(standard_array) == M:
        print(' '.join(map(str, standard_array)))
        return
    for i in range(start, N+1):
        standard_array.append(i)
        Solution(N, M, i)       # 시작지점을 현재 반복문을 돌고 있는 지점부터 지정한다면 문제에 부합하는 정답을 도출할 수 있다.
        standard_array.pop()

Solution(N, M, 1)