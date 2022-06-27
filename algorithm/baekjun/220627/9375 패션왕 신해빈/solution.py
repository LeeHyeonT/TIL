from re import A
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for _ in range(T):
    n = int(input())
    cloth_dict = dict()
    for _ in range(n):
        a, b = map(str, input().split())
        if b in cloth_dict:
            cloth_dict[b] += 1
        else:
            cloth_dict[b] = 1
    
    res = 1
    for i in cloth_dict.values():
        res *= (i+1)

    print(res-1)

# 옷 종류만 필요하지 이름까지는 필요가 없다!
# 종류가 겹칠 경우 dictionary의 value값을 +1 해주는 방식으로 진행