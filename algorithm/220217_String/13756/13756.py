import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# 테스트 횟수 입력받음
T = int(input())
# 테스트 횟수만큼 진행
for num in range(T):
    find = input()
    text = input()
    f_len = len(find)
    t_len = len(text)
    # 각각의 문자 담아놓을 dictionary 생성, 문자 담아놓고 value 0 으로 설정
    dic = {}
    for key in find:
        dic[key] = 0

    # 위에서 만든 dictionary 에 value 넣어줄 것
    # dictionary key 가 존재하지 않으면 KeyError 가 발생하기에 예외처리문으로 설정
    # .get 으로 진행해보기
    for i in text:
        try:
            dic[i] += 1
        except KeyError:
            continue
    # value 값들 중 가장 큰 것 꺼내오기
    max_cnt = 0
    for i in list(dic.values()):
        if i > max_cnt:
            max_cnt = i

    print(f"#{num+1} {max_cnt}")

    # cnt = 0
    # cnt_max = 0
    #
    # for i in range(f_len):
    #     for j in range(t_len):
    #        if find[i] == text[j]:
    #            cnt += 1
    # if cnt > cnt_max:
    #     cnt_max = cnt
    #
    # print(f"#{num+1} {cnt_max}")