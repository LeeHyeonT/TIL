import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# 모든 경우 안 돌아보는 코드 구해보기
# test case 가 10개이므로 10번 진행
for num in range(10):
    case = int(input())
    arr = [list(input()) for _ in range(100)]
    text_len = 0
    max_len = 0
    M = 2
    #
    while M <= 100:
        # 가로 탐색
        for i in range(100):
            for j in range(100 - M + 1):
                text = ""
                for k in range(M):
                    text += arr[i][j + k]

                if text == text[::-1]:
                    max_len = M
                    break

            if text == text[::-1]:
                break

        # 세로 탐색
        for i in range(100):
            for j in range(100 - M + 1):
                text = ""
                for k in range(M):
                    text += arr[j + k][i]
                if text == text[::-1]:
                    max_len = M
                    break
            if text == text[::-1]:
                break
        # 회문 길이를 1씩 늘려나감
        M += 1

    print(f"#{num+1} {max_len}")