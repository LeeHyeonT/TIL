import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
five = N // 5
tmp = 0
three = 0
count_lst = []

while True:
    count = 0
    
    namuzi = N % 5 + tmp * 5
    if namuzi % 3 == 0:
        three = namuzi // 3
        count += three
        count += five
        count_lst.append(count)
    
    if five == 0:
        break
    else:
        five -= 1
        tmp += 1
        continue

if count_lst:
    print(min(count_lst))
else:
    print(-1)


# 생각보다 바로 안 풀려서 당황했던 문제...
# 5로 나눈 몫부터 차례대로 나아가며 3으로 나눈 몫까지 확인



