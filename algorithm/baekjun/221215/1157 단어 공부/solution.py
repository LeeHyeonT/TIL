import sys
sys.stdin = open('input.txt', encoding='UTF-8')

word = input()
word_upper = word.upper()
word_dict = {}
for i in word_upper:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

result = ""
count = 0
for j in word_dict:
    if word_dict[j] > count:
        count = word_dict[j]
        result = j
    elif word_dict[j] == count:
        result = "?"
        
print(result)