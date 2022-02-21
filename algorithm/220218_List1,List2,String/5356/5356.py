import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 만큼 입력 받음
T = int(input())
# test case 만큼 반복
for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]
    # 새로운 단어나열 받을 것 생성
    new_word = ""
    # 행: 5개, 열: 1~15개 에서 반복
    for j in range(15):
        for i in range(5):
            # 행의 idx 요소가 전체 행 길이보다 작은 경우에만 그 값을 새로운 단어나열에 더해줌 
            if j < len(arr[i]):
                new_word += arr[i][j]

    print(f"#{tc} {new_word}")