import sys
sys.stdin = open('input.txt', encoding='UTF-8')

array = []
a, b, c = map(int, input().split())
array.append(a)
array.append(b)
array.append(c)
array.sort()
print(array[1])