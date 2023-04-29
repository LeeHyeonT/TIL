import sys
sys.stdin = open('input.txt', encoding='UTF-8')

string = input()
length = len(string)
if length < 10:
    print(string)
else:
    a = 1
    while True:
        if a*10 >= length:
            a -= 1
            break
        print(string[a*10 -10:a*10])
        a += 1
    print(string[a*10:length])

'''
Slicing 이용하면 쉬운 문제
'''