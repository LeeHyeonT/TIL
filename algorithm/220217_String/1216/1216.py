import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 가 10개이므로 10번 진행
for num in range(10):
    case = int(input())
    arr = [list(input()) for _ in range(100)]
    text_len = 0
    max_len = 0
    M = 2
    # 모든 경우를 돌아보기위해 길이가 2인 회문부터 길이가 100인 회문까지 검색
    while M <= 100:
        # 가로 탐색
        for i in range(100):
            for j in range(100 - M + 1):
                text = ""
                for k in range(M):
                    text += arr[i][j + k]
                # 회문이 맞다면 그 회문의 길이를 가져와서 저장
                # 저장한 값이 max 값인 경우 max 값에 다시 저장
                if text == text[::-1]:
                    text_len = len(text)
                    if text_len > max_len:
                        max_len = text_len
        # 세로 탐색
        for i in range(100):
            for j in range(100 - M + 1):
                text = ""
                for k in range(M):
                    text += arr[j + k][i]
                if text == text[::-1]:
                    text_len = len(text)
                    if text_len > max_len:
                        max_len = text_len
        # 회문 길이를 1씩 늘려나감
        M += 1

    print(f"#{num+1} {max_len}")