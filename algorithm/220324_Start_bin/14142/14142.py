import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(1,T+1):
    # 입력이 소수로 주어지므로 float 형태로 받아줌
    N = float(input())
    # 이진수 형태 저장할 bin, 소숫점 자리 계산할 cnt 생성
    bin = ""
    cnt = 0
    while True:
        # N 값에 계속 2를 곱하고 정수(1) 를 빼는 과정에서 N 이 0 이 되면 모든 과정 완료!
        if N == 0:
            print(f"#{tc} {bin}")
            break
        # 이러한 반복이 13번째가 된다면 overflow
        if cnt == 13:
            print(f"#{tc} overflow")
            break
        # N 에 2 곱하고 정수 존재하는지 확인
        N = N * 2
        if int(N) == 1:
            # 존재하면 이진수 값에 1 추가
            cnt += 1
            bin += str(1)
            N = N - 1
        # 존재하지 않는다면 이진수 값에 0 추가
        else:
            cnt += 1
            bin += str(0)

