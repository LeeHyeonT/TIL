import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())

if N >= 90:
    print('A')
elif N >= 80:
    print('B')
elif N >= 70:
    print('C')
elif N >= 60:
    print('D')
else:
    print('F')

# 문제 제대로 안 읽었다가 틀렸다
# 정신 차리자...힐링 문제 풀다가 틀라다니