import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# A, B = map(int, input().split())
# print(A+B)

# '''
# python은 이렇게 가능하지만 다른 언어라면?
# '''

A, B = map(str, input().split())
if len(A) > len(B):
    B = '0' * (len(A) - len(B)) + B
elif len(A) < len(B):
    A = '0' * (len(B) - len(A)) + A
answer = ''
upper = 0
num_sum = 0
for i in range(len(A)-1, -1, -1):
    num_A = A[i]
    num_B = B[i]
    # print(num_A, num_B)
    if int(num_A) + int(num_B) >= 10:
        upper = 1
    num_sum += (int(num_A) + int(num_B)) % 10
    answer = str(num_sum) + answer
    if i == 0 and upper == 1:
        answer = '1' + answer
    num_sum = upper
    upper = 0
print(int(answer))

'''
예제 답은 나오는데 답이 아닌 이유는...?
'''