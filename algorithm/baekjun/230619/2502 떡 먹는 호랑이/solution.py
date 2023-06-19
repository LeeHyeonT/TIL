import sys
sys.stdin = open('input.txt', encoding='UTF-8')

d, k = map(int, input().split())

pivo = [0] * (d-1)
pivo[0] = 1
pivo[1] = 1
for i in range(2, d-1):
    pivo[i] = pivo[i-2] + pivo[i-1]

a = 1
b = 1
while True:
    if (k - pivo[d-2] * b) % pivo[d-3] == 0:
        a = (k - pivo[d-2] * b) // pivo[d-3]
        if a <= b:
            break
    b += 1

print(a)
print(b)    

'''
Dynamic programming 문제 같으면서도 결국 수학 문제인 것이다
'''