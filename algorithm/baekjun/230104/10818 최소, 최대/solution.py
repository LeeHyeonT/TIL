sys.stdin = open('input.txt', encoding='UTF-8')
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

print(num_list[0], end=' ')
print(num_list[-1])

'''
- max, min 쓰는 것이 이 방법보다 덜 시간이 소요된다
- 처음에 int 형식을 배분하는 것이 아닌 for 문을 돌려 하나하나 int 형식을 배분하는 것이 메모리를 덜 소모한다
왜 그러는 것일까?? 궁금하다 궁금해
'''