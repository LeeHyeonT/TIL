import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    N, nums = map(str, input().split())
    # 이렇게 모든 16진법 숫자를 dictionary 로 표현할 시 0 꼭 들어가야 한다!
    hex_ten = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    # 일단 16진법을 10진법으로 바꿔서 저장
    str_10s = []
    for num in nums:
        str_10s.append(hex_ten[num])
    print(f"str_10s = {str_10s}")
    # 이후 2진법으로 바꾸기 위한 과정
    str_2s = []
    for str_10 in str_10s:
        # 10진법 수를 2로 나눠서 그 나머지를 저장할건데 그럼 구하고 싶은 값이 아닌
        # 거꾸로 나오므로 그걸 뒤집어줘야함
        str_2s_rev = []
        while True:
            str_2s_rev.append(str_10 % 2)
            str_10 = str_10 // 2
            if str_10 == 0:
                break
        str_2s_rev = str_2s_rev[::-1]
        print(f"0 추가 전 str_2s_rev = {str_2s_rev}")
        # 뒤집고 나서 전체 자리를 표현해줘야하기 때문에 4자리가 다 차있지 않다면
        # 앞부분에 0 추가
        if len(str_2s_rev) < 4:
            str_2s_rev = [0] * (4 - len(str_2s_rev)) + str_2s_rev
            print(f"0 추가 후 str_2s_rev = {str_2s_rev}")
        # 답 형태로 쉽게 나타내기 위해 위에서 구한 값을 str 형태로 저장
        str_2s_rev_str = ""
        for i in str_2s_rev:
            str_2s_rev_str += str(i)
        # str 형태의 값들을 저장해주면 끝!
        str_2s.append(str_2s_rev_str)
    print(str_2s)
    print(f"#{tc} {''.join(str_2s)}")