import sys
sys.stdin = open('input.txt', encoding='UTF-8')


N = int(input())
num_set = set()
target = '666'
# 3자리
num_set.add(int(target))
# 4자리
# 1 0 
for m1 in range(1,10):
    num_str = str(m1) + target
    num = int(num_str)
    num_set.add(num)
# 0 1
for m2 in range(0, 10):
    num_str = target + str(m2)
    num = int(num_str)
    num_set.add(num)

# 5자리
# 2 0
for m3 in range(10, 100):
    num_str = str(m3) + target
    num = int(num_str)
    num_set.add(num)
# 1 1
for m4 in range(1, 10):
    for n1 in range(0, 10):
        num_str = str(m4) + target + str(n1)
        num = int(num_str)
        num_set.add(num)
# 0 2
for n2 in range(0, 10):
    for n3 in range(0, 10):
        num_str = target + str(n2) + str(n3)
        num = int(num_str)
        num_set.add(num)

# 6자리
# 3 0
for m5 in range(100, 1000):
    num_str = str(m5) + target 
    num = int(num_str)
    num_set.add(num)
# 2 1
for m6 in range(10, 100):
    for n4 in range(0, 10):
        num_str = str(m6) + target + str(n4)
        num = int(num_str)
        num_set.add(num)
# 1 2
for m7 in range(1, 10):
    for n5 in range(0, 10):
        for n6 in range(0, 10):
            num_str = str(m7) + target + str(n5) + str(n6)
            num = int(num_str)
            num_set.add(num)
# 0 3
for n7 in range(0, 10):
    for n8 in range(0, 10):
        for n9 in range(0, 10):
            num_str = target + str(n7) + str(n8) + str(n9)
            num = int(num_str)
            num_set.add(num)

# 7자리
# 4 0
for m8 in range(1000, 10000):
    num_str = str(m8) + target 
    num = int(num_str)
    num_set.add(num)
# 3 1
for m9 in range(100, 1000):
    for n10 in range(0, 10):
        num_str = str(m9) + target + str(n10)
        num = int(num_str)
        num_set.add(num)
# 2 2
for m10 in range(10, 100):
    for n11 in range(0, 10):
        for n12 in range(0, 10):
            num_str = str(m10) + target + str(n11) + str(n12)
            num = int(num_str)
            num_set.add(num) 
# 1 3
for m11 in range(1, 10):
    for n13 in range(0, 10):
        for n14 in range(0, 10):
            for n15 in range(0, 10):
                num_str = str(m11) + target + str(n13) + str(n14) + str(n15)
                num = int(num_str)
                num_set.add(num)
# 0 4
for n16 in range(0, 10):
    for n17 in range(0, 10):
        for n18 in range(0, 10):
            for n19 in range(0, 10):
                num_str = target + str(n16) + str(n17) + str(n18) + str(n19)
                num = int(num_str)
                num_set.add(num)

num_sort = sorted(num_set)
print(num_sort[N-1])

# 이걸로 답 냈음...
# 모든 경우를 그냥 다 돌아버렸는데 이건 별로 효율적이지 못한 방법
# 라고 생각했는데 제출한 것들 보니 시간은 엄청 효율적인 것 같음!
