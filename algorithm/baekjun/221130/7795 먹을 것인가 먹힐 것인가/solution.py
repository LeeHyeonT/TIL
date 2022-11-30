from itertools import product
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # '''
    # 약간 효율적인 방법
    # python3: 시간초과
    # pypy3: 통과
    # '''
    # sort_A = sorted(A)
    # sort_B = sorted(B)
    # count = 0
    # for a in sort_A:
    #     for b in sort_B:
    #         if a < b:
    #             break
    #         elif a > b:
    #             count += 1
    # print(count)

    # '''
    # 약간 효율적인 방법2
    # python3: 시간초과
    # pypy3: 통과
    # '''
    # A.sort()
    # B.sort()
    # count = 0
    # for a in A:
    #     for b in B:
    #         if a < b:
    #             break
    #         elif a > b:
    #             count += 1
    # print(count)
    '''
    효율적인 방법 2
    python3: 시간초과
    pypy3: 통과 ㅁ
    '''
    A.sort()
    B.sort()
    result = 0
    for i in range(len(A)):
        count = 0
        while True:
            if count == len(B) or A[i] <= B[count]:
                result += count
                break
            else:
                count += 1
    print(result)

    # '''
    # Brutal force test
    # --> 당연히 안 됨 시간초과!
    # '''
    # count = 0
    # for a in A:
    #     for b in B:
    #         if a > b:
    #             count += 1

    # '''
    # 내장 조합 함수 사용
    # --> 메모리 초과로 인한 실패!
    # '''
    # test = []
    # test.append(A)
    # test.append(B)
    # results = list(product(*test))
    # count = 0
    # for result in results:
    #     if result[0] > result[1]:
    #         count += 1
    # print(count)

    '''
    이진 탐색으로도 가능!
    기준에 되는 A 값을 B list 에 이진탐색 돌려서 거기서 기준 A의 index 값이 결국 순서쌍 갯수가 된다!
    이게 좋은 방법인 듯 싶다
    '''
