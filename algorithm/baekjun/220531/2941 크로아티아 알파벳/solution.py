import sys
sys.stdin = open('input.txt', encoding='UTF-8')

ref2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
ref3 = 'dz='

get_str = input()
cnt = 0
cursor = 0
past_cursor = 0
while cursor < len(get_str):
    past_cursor = cursor
    
    for j in ref2:
        if get_str[cursor:cursor+2] == j:
            print(get_str[cursor:cursor+2])
            cnt += 1
            cursor += 2
            break
    else:
        if get_str[cursor:cursor+3] == ref3:
            print(get_str[cursor:cursor+3])
            cnt += 1
            cursor += 3
            
    if cursor == past_cursor:
        cnt += 1
        cursor += 1
               


print(cnt)

# break 때문에 고생함...
# else 부분에 break 넣으면 while 문이 끝나는 불상사가 발생
# 진짜 다 까먹은 것 같음....천천히 복습해나가자
# 아~ 마~ 아 존조로 존조로 존~
