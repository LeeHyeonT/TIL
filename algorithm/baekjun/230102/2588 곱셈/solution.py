import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

multiple_1 = int(input())
multiple_2 = input()
answer_list = []
for i in range(len(multiple_2)-1, -1, -1):
    answer_list.append(multiple_1 * int(multiple_2[i]))

answer = 0
digit = 1

for num in answer_list:
    answer += num * digit
    if digit == 100:
        break
    digit *= 10
for j in answer_list:
    print(j)
print(answer)