import sys
sys.stdin = open('input.txt', encoding='UTF-8')

word = input()
l = len(word)
for i in range(l // 2):
    a = word[i]
    b = word[l-1-i]
    if a == b:
        continue
    else:
        print(0)
        break
else:
    print(1)
    

'''
절반만 확인해봄으로써 시간을 절약할 수 있도록 함
'''