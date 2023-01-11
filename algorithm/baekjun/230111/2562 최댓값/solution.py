import sys
sys.stdin = open('input.txt', encoding='UTF-8')

max_num = 0
index = -1
for i in range(1,10):
    number = int(input())
    if max_num < number:
        max_num = number
        index = i

print(max_num)
print(index)
