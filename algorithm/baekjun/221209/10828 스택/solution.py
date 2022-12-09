sys.stdin = open('input.txt', encoding='UTF-8')
import sys
input = sys.stdin.readline

N = int(input())
stack = []
index = -1
for _ in range(N):
    commands = list(input().split())
    # 명령어가 push 인지 아닌지 구분
    if commands[0] == 'push':
        command = commands[0]
        number = int(commands[1])
    else:
        command = commands[0]
    
    # 명령어 정리
    if command == 'push':
        stack.append(number)
        index += 1
    elif command == 'pop':
        if index < 0:
            print(-1)
        else:
            print(stack[index])
            stack = stack[0:index]
            index -= 1
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if index < 0:
            print(1)
        else:
            print(0)
    elif command =='top':
        if index < 0:
            print(-1)
        else:
            print(stack[index])

'''
stack... 예전에 배울 때 재밌게 배웠던 기억이 있다
아직 그 기억이 다 사라지지 않아서 다행이다
'''