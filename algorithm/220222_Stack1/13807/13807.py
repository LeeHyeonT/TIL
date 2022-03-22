import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 받아옴
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    # 값 받아올 stack, 그에 따른 top 값 설정
    stack = []
    words = input()
    top = -1
    # 글자열 길이만큼 반복
    for i in range(len(words)):
        # (, { 인 경우에만 stack 에 더해줌, top 값은 그에 맞게 올라감
        if words[i] =="(" or words[i] == "{":
            stack.append(words[i])
            top += 1
        # ) 인 경우:
        # 1) stack 이 비어있는 경우
        # 2) stack의 마지막 값이 ( 가 아닌 경우
        # 이 두 가지 경우에 대해서 안되므로  각각의 경우에 대하여 stack 에 이상한 값을 더함으로써 처리
        # 올바른 경우라면 ( (stack 마지막 부분) 지우고 top 값도 내림
        elif words[i] == ")":
            if top != -1:
                if stack[top] == "(":
                    stack.pop()
                    top -= 1
                else:
                    stack.append(")")
                    top += 1
            else:
                stack.append("임의")
                top += 1
                
        # { 도 ( 와 같은 방식으로 진행
        elif words[i] == "}":
            if top != -1:
                if stack[top] == "{":
                    stack.pop()
                    top -= 1
                else:
                    stack.append("}")
                    top += 1
            else:
                stack.append("}")
                top += 1

    # stack 이 비어있으면 성공, 아니면 실패
    if len(stack) == 0:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
    # toggle
    # ^=
    # x = 1             x= 0
    # x ^= 1            x ^= 1
    # print(x) : 0      print(x) : 1
