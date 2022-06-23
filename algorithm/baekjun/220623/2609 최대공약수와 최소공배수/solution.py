from math import lcm
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# gcf lcm
M, N = map(int,input().split())

GCF = 0
LCM = 0
if M > N:
    tmp_small = N
    tmp_big = M
else:
    tmp_small = M
    tmp_big = N

while True:
    if GCF != 0:
        break
    
    if M % tmp_small == 0 and N % tmp_small == 0:
        GCF = tmp_small
    
    tmp_small -= 1

while True:
    if LCM != 0:
        break

    if tmp_big % M == 0 and tmp_big % N == 0:
        LCM = tmp_big
    
    tmp_big += 1

print(GCF)
print(LCM)