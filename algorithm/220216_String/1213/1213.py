import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# test case 가 10개이므로 10번 실행
for num in range(10):
    case = int(input())
    find = input()
    text = input()
    f_len = len(find)
    t_len = len(text)
    cnt = 0
    # find 값이 text 내에 있는지 확인: text 길이에서 find 길이만큼 뺀 만큼 실행
    for i in range(t_len - f_len + 1):
        # find 값을 text 에서 찾았다면 count 하나 더해줌
        if text[i:f_len + i] == find:
            cnt += 1

    print(f"#{num+1} {cnt}")


