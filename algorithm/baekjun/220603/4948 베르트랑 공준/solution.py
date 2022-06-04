import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def prime(n):
    prime_check = [True] * (123456 * 2 +1)
    prime_check[0] = False
    prime_check[1] = False

    for i in range(2, 2*n+1):
        if prime_check[i] == True:
            j = 2

            while (i*j) <= 2*n:
                prime_check[i*j] = False
                j += 1
    return prime_check


num_arr = []
while True:
    num = int(input())
    if num == 0:
        break
    num_arr.append(num)

count_arr = []
for k in num_arr:
    prime_arr = prime(k)
    count = 0
    for l in prime_arr[k+1:2*k+1]:
        if l == True:
            count += 1
    count_arr.append(count)

for m in count_arr:
    print(m)


# 에라토스테네스의 채...를 다시 알게 되었다.
# 시간과의 싸움이 시작되었다.