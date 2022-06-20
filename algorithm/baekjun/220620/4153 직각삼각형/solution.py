import sys
sys.stdin = open('input.txt', encoding='UTF-8')

while True:
    a, b, c = map(int, input().split())
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    if a == 0 and b == 0 and c == 0:
        break   
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print('right')
    else:
        print('wrong')

# 이 정도 문제라면 sort 부담없이 써도 된다!
# while문 오랜만이었는데 무한루프 안 돌도록 조심하자!
    