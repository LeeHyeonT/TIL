import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    nod_num = int(input())
    # 알파벳, 노드 기준 왼쪽, 오른쪽 저장할 리스트 생성
    ch = [None] * (nod_num + 1)
    ch_L = [0] * (nod_num + 1)
    ch_R = [0] * (nod_num + 1)

    for i in range(nod_num):
        input_list = list(input().split())

        # input 값이 제각기 다르기에 각 경우에 따라 처리 방식 나뉨
        if len(input_list) == 4:
            ch[i+1] = input_list[1]
            ch_L[i+1] = int(input_list[2])
            ch_R[i+1] = int(input_list[3])
        elif len(input_list) == 3:
            ch[i+1] = input_list[1]
            ch_L[i+1] = int(input_list[2])
        elif len(input_list) == 2:
            ch[i+1] = input_list[1]
    
    # 순회 돌고 나오는 단어 담아줄 리스트 생성
    letter_list = []
    # 중위순회 정의
    def inorder(T):
        if T != 0:
            inorder(ch_L[T])
            letter_list.append(ch[T])
            inorder(ch_R[T])
    # 중위순회 실시 및 출력
    inorder(1)
    print(f"#{tc}", "".join(letter_list))
