sys.stdin = open('input.txt', encoding='UTF-8')
import sys
input = sys.stdin.readline

def vps():
    stack = []
    ps = input().strip()
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(0)
        elif ps[i] == ')':
            if len(stack) == 0:
                print('NO')
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO') 


N = int(input())
for _ in range(N):
    vps()



# stack = []
# ps = input().strip()
# for i in range(len(ps)):
#     if ps[i] == '(':
#         stack.append(0)
#     elif ps[i] == ')':
#         if len(stack) == 0:
#             print('NO')
#             break
#         else:
#             stack.pop()
# print(stack)
# if len(stack) == 0:
#     print('YES')
# else:
#     print('NO') 