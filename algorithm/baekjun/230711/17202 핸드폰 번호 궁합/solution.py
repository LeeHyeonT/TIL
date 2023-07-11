import sys
sys.stdin = open('input.txt', encoding='UTF-8')

a = input()
b = input()
storage = []
for i in range(8):
    storage.append(int(a[i]))
    storage.append(int(b[i]))

while True:
    if len(storage) == 2:
        break
    answer = []
    
    for j in range(len(storage)-1):
        num = storage[j] + storage[j+1]
        if num >= 10:
            num -= 10
        answer.append(num)
    
    storage = answer
    
for ans in answer:
    print(ans, end='')
    
    
'''
이게 왜 Dynamic Programming 문제인 지 모르겠다...
'''