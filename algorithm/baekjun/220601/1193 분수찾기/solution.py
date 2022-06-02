import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
line = 0
# 라인 찾기
while n > line:
    n -= line
    line += 1

# 홀수라인 vs 짝수라인
print(line)
print(n)

if line % 2  == 1:
    a = line - n + 1
    b = n
else:
    a = n
    b = line - n + 1

print(a, end='')
print('/',end='')
print(b)