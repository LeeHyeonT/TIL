import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
line_array = []
for _ in range(K):
    line_array.append(int(input().rstrip()))

start = 1
end = max(line_array)

while True:
    
    if start > end:
        break
    
    cnt = 0
    middle = (start + end) // 2 

    for line in line_array:
        cnt += (line // middle)
    
    if cnt >= N:
        start = middle + 1
        answer = middle
        
    if cnt < N:
        end = middle - 1
    
print(answer)

            
'''
계속 50% 구간에서 틀려 애먹었던 문제
일단 binary search 자체를 조금 이상하게 사용하고 있었다!
start 랑 end 부분 갱신할 때 middle 로 갱신하는 것이 아닌 -1 / +1 을 주어야 했다
또한 초기 start 값을 0이 아닌 1로 해야했다
'''
        