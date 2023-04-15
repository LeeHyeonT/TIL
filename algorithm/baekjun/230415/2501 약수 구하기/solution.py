import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, k = map(int, input().split())
ans_list = []
for i in range(1, n+1):
    if n % i == 0:
        ans_list.append(i)
if len(ans_list) < k:
    print(0)
else:
    print(ans_list[k-1])

'''
input 값이 적으면 생각보다 시간이 적게 나온다.
반복할 수 있는 최댓값은 10,000 인데 시간은 44ms 정도 나오니 input 갯수가 10,000 개일 때에 비해 시간이 적게 나오는 것을 확인 가능하다.
'''