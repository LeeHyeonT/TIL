import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
queue = []
start = -1
end = -1
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
        queue.append(number)
        if start == -1:
            start += 1
        end += 1
    elif command == 'pop':
        if end < 0 or start > end:
            print(-1)
        else:
            print(queue[start])
            start += 1
    elif command == 'size':
        print(len(queue) - start)
    elif command == 'empty':
        if end < 0 or len(queue) - start == 0:
            print(1)
        else:
            print(0)
    elif command =='front':
        if end < 0 or len(queue) - start == 0:
            print(-1)
        else:
            print(queue[start])
    elif command == 'back':
        if end < 0 or len(queue) - start == 0:
            print(-1)
        else:
            print(queue[end])

'''
시간초와의 싸움
pop 같은 것을 활용한다면 새로이 list를 만들게 되는 것인데
그렇게 계속 새로운 list를 만들고 지우고 하다보면 시간초과가 발생
따라서 실제 list는 하나로 두고 시작, 끝 index를 잡은 뒤
여기서 말하는 pop 이 일어난 경우 시작 index 를 하나 땡겨 생격하는 식으로 진행
'''