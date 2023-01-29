import sys
sys.stdin = open('input.txt',encoding='UTF-8')

answer_dict = {}
for _ in range(10):
    num = int(input())
    if num % 42 in  answer_dict:
        answer_dict[num % 42] += 1
    else:
        answer_dict[num % 42] = 1

print(len(answer_dict))


'''
1차원 배열 쪽에 있는 문제지만
따로 dictionary 쪽 문제가 없기에
이걸로 풀어봄
'''