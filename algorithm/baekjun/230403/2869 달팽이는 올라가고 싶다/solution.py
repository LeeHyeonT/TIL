import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a, b, v = map(int, input().split())
if a == v:
    print(1)
else:
    if (v-b) / (a-b) > int((v-b) / (a-b)):
        print(int((v-b) / (a-b)) + 1)
    else:
        print(int((v-b) / (a-b)))
