import sys
sys.stdin = open('input.txt', encoding='UTF-8')

all = int(input())
for _ in range(9):
    price = int(input())
    all -= price

print(all)