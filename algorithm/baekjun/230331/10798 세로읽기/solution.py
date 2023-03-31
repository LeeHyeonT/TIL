import sys
sys.stdin = open('input.txt', encoding='UTF-8')

array = []
for _ in range(5):
    word = input()
    word = word + '-' * (15 - len(word))
    array.append(word)

for i in range(15):
    for j in range(5):
        if array[j][i] == '-':
            continue
        else:
            print(array[j][i], end='')