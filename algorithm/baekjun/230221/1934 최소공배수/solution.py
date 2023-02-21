import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

def Euclidean(A,B):
    global num
    C = max(A, B) % min(A, B)
    if C == 0:
        num = min(A,B)
        return min(A,B)
    else:
        Euclidean(C, min(A,B))
        
T = int(input())
for _ in range(T):
    A, B = map(int, input().rstrip().split())
    num = 0
    Euclidean(A,B)
    print((A // num) * (B))
    

'''
유클리드 호제법에 대해 알 수 있었다!
오랜만에 봤는데 신기하다... 오랜만이야 호제법
'''