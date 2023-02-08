import sys
sys.stdin = open('input.txt', encoding='UTF-8')


M, N = map(int, input().split())
array = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        array.append(i)

for num in array:
    print(num)

'''
정수론에 따르면 소수를 판별할 때 굳이 전체 숫자를 다 파악하지 않아도 되고
파악하고자 하는 숫자의 제곱근 만큼만 판별하여도 된다고 한다!
명심하도록!

한 번 틀렸다... edge case 고려안함
수정: 자꾸 1을 넣길래 1을 빼줌
'''