import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 최대 500,500번 반복하는 문제?

string = input()
answer_set = set()
len_count = 1
while True:
    if len_count > len(string) - 1:
        break
    
    for i in range(len(string) - len_count + 1):
        word = ''
        present_len = 0
        while True:
            if present_len > len_count - 1:
                break
            word += string[i + present_len]
            present_len += 1
       
        answer_set.add(word)
    len_count += 1

print(len(answer_set) + 1)

'''
시간초과 나오는 로직
하....머리 안 돌아가서 늦게 풀었건만 시간초과네 이런....
+ 맨 마지막 문자열은 무조건 서로 다른 문자열로 들어가기에 그건 빼고 셌지만 실패!

'''