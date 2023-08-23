import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # 첫 번째 방법
    num_array = list(map(int, input().rstrip().split()))
    print(min(num_array), end=' ')
    print(max(num_array))
    # 두 번째 방법
    num_array = list(map(int, input().rstrip().split()))
    num_array.sort()
    print(num_array[0], end=' ')
    print(num_array[-1])
    

'''
첫 번째 방법: 964ms
두 번째 방법: 1780ms

역시 sort 하는 과정에서 시간을 많이 빼앗는 것 같다. 이후 list 탐색에 있어선 index 탐색이 min, max 탐색보다 훨씬 빠를텐데 말이다.
'''