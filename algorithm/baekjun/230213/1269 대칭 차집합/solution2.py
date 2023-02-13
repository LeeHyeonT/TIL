import sys
sys.stdin = open('input.txt', encoding='UTF-8')

nA, nB = map(int, input().split())

A = input().split()
B = input().split()

# diagram_array = list(set(A + B))
# only_A = list(i for i in diagram_array if i not in B)
# only_B = list(j for j in diagram_array if j not in A)
# print(len(only_A) + len(only_B))

diagram_array = A+B
common_cnt = 0
while True:
    if len(diagram_array) <= nB:
        break
    number = diagram_array.pop(0)
    if number in diagram_array:
        common_cnt += 1
  
answer = len(A+B) - 2 * common_cnt
print(answer)


'''
set도 활용하되 list 를 메인으로 활용하여 문제를 풀어보고자 했으나 효율적인 방법이 도저히 나오지 않음...
'''