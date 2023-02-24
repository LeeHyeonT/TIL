import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    commands = input().rstrip()
    n = int(input())
    nums = input().rstrip()
    # array에 숫자들 넣는 과정
    nums_array = []
    a = ''
    for num in nums:
        if num != '[' and num != ']' and num != ',':
            a += num
        if (num == ',' or num == ']') and a:
            nums_array.append(int(a))
            a = ''
       
       
    # command 갈무리 과정
    ignore_list = []
    i = 0
    while True:
        if i >= len(commands) - 1:
            break
        
        if commands[i] == commands[i+1] == 'R':
            ignore_list.append(i)
            ignore_list.append(i+1)
            i += 2
        else:
            i += 1
   # 진행
    for j in range(len(commands)):
        if j in ignore_list:
            continue
        else:
            if commands[j] == 'R':
                nums_array.reverse()
            elif commands[j] == 'D':
                if len(nums_array) == 0:
                    print('error')
                    break
                else:
                    nums_array = nums_array[1:n]
                    n -= 1
    # 정답 만들기
    if len(nums_array):
        ans_array = '['
        for k in range(len(nums_array)):
            if k == len(nums_array) - 1:
                ans_array += str(nums_array[k])
                ans_array += ']'
            else:
                ans_array += str(nums_array[k])
                ans_array += ','
        print(ans_array)
        

'''
시간 초과가 나오는 상황...
파싱으로 해결될까싶어 deque 말고 array 자체를 parsing 하는 방법으로도 해봤지만 시간초과의 늪을 벗어날 수는 없었다
'''