import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

def vps():
    stack = []
    ps = input().rstrip()
    if ps == '.':
        exit()
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append('(')
        elif ps[i] == ')':
            if len(stack) == 0:
                print('no')
                return
            else:
                if stack[-1] != '(':
                    print('no')
                    return
                else:
                    stack.pop()

        if ps[i] == '[':
            stack.append('[')
        elif ps[i] == ']':
            if len(stack) == 0:
                print('no')
                return
            else:
                if stack[-1] != '[':
                    print('no')
                    return
                else:
                    stack.pop()
                    
    if len(stack) != 0:
        print('no')
    else:
        print('yes')

while True:
    vps()


'''
sys.stdin.readline 으로 input 받아올 때는 꼭 .rstrip() 처리를 하자!
'''

