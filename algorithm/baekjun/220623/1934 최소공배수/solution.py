import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
for _ in range(N):
    num1, num2 = map(int, input().split())

    if num1 % num2 == 0 or num2 % num1 == 0:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    else:
        GCD = 2
        while True:
            if num1 % GCD == 0 and num2 % GCD == 0:
                break
            GCD += 1
            if num1 > num2:
                if GCD >= num2:
                    GCD = 1
                    break
            else:
                if GCD >= num1:
                    GCD = 1
                    break   

        print(round(num1 * num2 / GCD)) 