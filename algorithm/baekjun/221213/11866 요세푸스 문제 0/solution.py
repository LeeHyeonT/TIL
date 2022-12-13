import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N, K = map(int, input().split())    
array = []
for i in range(1, N+1):
    array.append(i)

answer = []
trigger = 0    
while True:
    if sum(array) == 0:
        break
    count = 0
    while True:
        if array[trigger % N] != 0:
            count += 1
        if count == K:
            break   
        trigger += 1
      
    i = trigger % N        

    answer.append(array[i])
    array[i] = 0
print('<', end='')
for j in range(len(answer)):
    if j == len(answer) -1:
        print(answer[j], end='')
    else:
        print(answer[j], end=', ')
print('>')