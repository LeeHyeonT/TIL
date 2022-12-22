import sys
sys.stdin = open('input.txt', encoding='UTF-8')

M = int(input())
N = int(input())

array = []

for i in range(M, N+1):
	for j in range(2, i+1):
        # 1과 자기 자신만 나눠떨어지기에 이런 조건으로
		if j == i:
			array.append(i)
        # 어떤 숫자로 나눠서 나머지가 0이 되면 소수가 아니게되므로    
		if i % j == 0:
			break

if array == []:
	print(-1)
else:
	print(sum(array))
	print(array[0])