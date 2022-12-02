import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N, K = map(int, input().split())
temp_lists = list(map(int, input().split()))


def Function(length):
    global result
    i = 0
    result_sum = 0
    count = 0
    '''
    초기값 설정하는 것 주의해서 하자!
    최대 100,000 개에 한 온도 당 -100 까지 가능하니 초기값이 100,000 * -100 보단 작아야한다!
    '''
    result = -999999999
    while True:
        if i == N:
            break
        result_sum += temp_lists[i]
        count += 1
        i += 1
        print(i, count)

        if count == length:
            if i == N:
                if result < result_sum:
                    result = result_sum
                    break
            else:
                if result < result_sum:
                    result = result_sum
            count = 0
            result_sum = 0
            i -= (length - 1)


Function(K)
print(result)
