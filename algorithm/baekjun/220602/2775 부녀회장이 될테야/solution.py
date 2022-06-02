import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def sumsum(k, n):
    global count
    if k == 0:
        count += n
        return 

    for i in range(1,n+1):
        sumsum(k-1, i)    



T = int(input())
for _ in range(1, T+1):
    k = int(input())
    n = int(input())
    count = 0
    sumsum(k, n)
    print(count)
