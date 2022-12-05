import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

expression = input()
number_str = [""] * 30
index = 0
while True:
    for j in range(len(expression)):
        if expression[j] == "+" or expression[j] == "-":
            index += 1
        number_str[index] += expression[j]
    else:
        break


number_list = [0] * 30
for k in range(len(number_str)):

    if number_str[k] == '':
        break
    if int(number_str[k]) < 0:
        kk = k
        while True:
            if kk == len(number_str) or number_str[kk] == '':
                kk += 1
                break
            number_list[kk] = -abs(int(number_str[kk]))
            kk += 1
    if number_list[k] == 0 and number_list[k] >= 0:
        number_list[k] += int(number_str[k])

print(sum(number_list))
