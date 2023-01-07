import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = input()
count = 0
for i in range(1, int(N)+1):
    if i < 100:
        count += 1
    else:
        i_string = str(i)
        if int(i_string[0]) - int(i_string[1]) == int(i_string[1]) - int(i_string[2]):
            count += 1
        elif int(i_string[1]) - int(i_string[0]) == int(i_string[2]) - int(i_string[1]):
            count += 1
        elif i_string[0] == i_string[1] == i_string[2]:
            count += 1

print(count)

'''
숫자가 1000 이하 까지라 쉬운 느낌인데 그게 아니라면 단순 조건식 말고 함수식으로 표현해야할듯
'''