import sys
sys.stdin = open('input.txt',encoding='UTF-8')

attendence = []
for i in range(1, 31):
    attendence.append(i)

for _ in range(28):
    attendence.remove(int(input()))
    
for num in attendence:
    print(num)
