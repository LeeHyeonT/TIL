import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a = int(input())
b = int(input())
c = int(input())
num = str(a*b*c)
num_storage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for n in num:
    num_storage[int(n)] += 1

for ans in num_storage:
    print(ans)
    

'''
python 에서만 쓸 수 있는 dictionary 구조 말고 array 구조로 풀려면 이렇게 풀어야
'''