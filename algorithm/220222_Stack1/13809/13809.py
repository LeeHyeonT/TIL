import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 갯수 입력
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    # 문자 저장해 줄 stack list 생성
    stack = []
    words = input()
    # 초기 top 값을 -1로 설정
    top = -1
    # words 길이만큼 반복
    for i in range(len(words)):
        # stack 에 단어 하나하나 떼어서 더해줌
        # 비교 먼저해도 가능!
        stack.append(words[i])
        # 단어 하나 더해질 때마다 top 값도 하나 더해줌
        top += 1
        # 반복 문자가 존재하려면 일단 stack 길이가 2 이상이어야 하고
        # 반복 문자가 나왔다면 처리
        if len(stack) >= 2 and stack[top-1] == stack[top]:
            # 끝의 두 개의 문자 삭제
            stack.pop()
            stack.pop()
            # 문자 두 개 삭제되었으니 top 값도 -2 해줌
            top -= 2
    # stack 내 남은 문자들의 길이를 활용하여 출력
    print(f"#{tc} {len(stack)}")