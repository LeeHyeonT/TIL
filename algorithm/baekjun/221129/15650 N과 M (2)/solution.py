import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())


# 1~N 까지 반복문
# 빈 array 에 반복문 값 넣어줌
# 중복 확인 후 중복이면 마지막에 넣은 값 뺌
# 만약 길이가 M 이라면 새로운 배열 시작
# 마지막 넣은 값이 N 이라면
# 다음 반복문은 1 더한 값부터 N까지 반복
# 이대로 반복, 1 더한 값이 N 이 나올 때까지

s = []


def Sequence(N, M, start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            Sequence(N, M, i+1)
            s.pop()


Sequence(N, M, 1)
''' 
# 오류 1: M 값이 1일 때 발생하는 오류
해결 완료
M == 1 일 때 분기처리하여 해결
하지만 못 쓰는 정보가 되어버림
# 오류 2: 모든 경우를 돌지 못하는 오류
해결 미완료
다른 방법으로 문제 풀어 이 오류는 해결 못한 상태로 남음...
'''
