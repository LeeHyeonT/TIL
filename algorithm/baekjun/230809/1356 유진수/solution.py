import sys
sys.stdin = open('input.txt', encoding='UTF-8')

num = input()
num_len = len(num)
if num_len == 1:
    print('NO')
else:
    ans1 = 1
    ans2 = 1
    for i in range(1, num_len):
        for j in range(0, i):
            ans1 *= int(num[j]) 
        for k in range(i, num_len):
            ans2 *= int(num[k])
        if ans1 == ans2:
            print('YES')
            break
        else:
            ans1 = 1
            ans2 = 1
    else:
        print('NO')