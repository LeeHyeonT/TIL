import sys
sys.stdin = open('input.txt', encoding='UTF-8')

arr = list(map(str, input().split()))

num1 = arr[0]
num1_rev = []
num2 = arr[1]
num2_rev = []
for i in range(len(num1)-1,-1,-1):
    num1_rev.append(num1[i])
for j in range(len(num2)-1,-1,-1):
    num2_rev.append(num2[j])

# print(type(''.join(num1_rev)))
if len(num1_rev) > len(num2_rev):
    print(int(''.join(num1_rev)))
elif len(num1_rev) < len(num2_rev):
    print(int(''.join(num2_rev)))
else:
    a = 0
    while True:
        if int(num1_rev[a]) > int(num2_rev[a]):
            print(int(''.join(num1_rev)))
            break
        elif int(num1_rev[a]) < int(num2_rev[a]):
            print(int(''.join(num2_rev)))
            break
        else:
            a += 1
