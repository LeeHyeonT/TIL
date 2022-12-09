sys.stdin = open('input.txt', encoding='UTF-8')
import sys
input = sys.stdin.readline

K = int(input())
stack = []
index = -1
# '''
# pop 안 쓰고 하기
# 메모리 31696 KB
# 시간 4908 ms 
# '''
# for _ in range(K):
#     num = int(input())
#     if  num == 0:
#         stack = stack[0:index]
#         index -= 1
#     else:
#         stack.append(num)
#         index += 1
# print(sum(stack))

'''
pop 쓰고 하기
메모리 31256 KB
시간 84ms
'''
for _ in range(K):
    num = int(input())
    if  num == 0:
        stack.pop()
        index -= 1
    else:
        stack.append(num)
        index += 1
print(sum(stack))