import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
target = '666'
num_set = set()
for i in range(0, 100):
    for j in range(0, 100):
        num_str = str(i) + target + str(j)
        num = int(num_str)
        num_set.add(num)

for k in range(0, 10000):
    num_str = str(k) + target
    num = int(num_str)
    num_set.add(num)

for l in range(0, 10000):
    num_str = target + str(l) 
    num = int(num_str)
    num_set.add(num)

for m1 in range(0, 1000):
    for n1 in range(0, 10):
        num_str = str(m1) + target + str(n1) 
        num = int(num_str)
        num_set.add(num)

for m2 in range(0, 10):
    for n2 in range(0, 1000):
        num_str = str(m2) + target + str(n2) 
        num = int(num_str)
        num_set.add(num)

num_sort = sorted(num_set)
print(num_sort)