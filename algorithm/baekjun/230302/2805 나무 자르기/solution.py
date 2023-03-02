import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

def BinarySearch(start, end):
    global answer
    while True:
        if start > end:
            break
    
        middle = (start  + end) // 2
        cnt = 0
        for tree in tree_array:
            a = tree - middle
            if a <= 0:
                continue
            else:
                cnt += a
        
        if cnt >= M:
            start = middle + 1
            answer = middle

        elif cnt < M:
            end = middle - 1
    
N, M = map(int, input().rstrip().split())
tree_array = list(map(int, input().rstrip().split()))

start = 0
end = max(tree_array)

BinarySearch(start, end)
print(answer)
# while True:
#     if start > end:
#         break
    
#     middle = (start  + end) // 2
#     cnt = 0
#     for tree in tree_array:
#         a = tree - middle
#         if a <= 0:
#             continue
#         else:
#             cnt += a
    
#     if cnt >= M:
#         start = middle + 1
#         answer = middle
#     elif cnt < M:
#         end = middle - 1

# print(answer)

'''
일반적인 while 반복문으로 진행하면 python3 인코딩으론 시간 초과가 난다
일반적으로 python 코드는 기본 반복문보다 함수 내에서의 반복문이 더 빠르게 실행된다
따라서 이 문제같은 경우 함수 내에 반복문을 넣어 python3 인코딩 시간 초과를 해결할 수 있다
(pypy3 인코딩으로는 그냥 정답이긴 하다)
'''