import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# 몇 번 실행할지 숫자로 받음
T = int(input())
# 입력맏은 숫자만큼 실행
for num in range(T):
    A, B = input().split()
    len_A = len(A)
    len_B = len(B)
    cnt = 0
    ni = 0
    # A 문자를 B의 길이만큼 확인: 확인한 것과 B가 같다면 count 1 더해주고 그 문자는 뛰어넘어야하기에
    # ni += len_B를 실행
    # 아닌 경우에는 ni 에 1 더해줘 다음 나열 확인
    while ni <= len_A - len_B:
        if A[ni:len_B+ni] == B:
            cnt += 1
            ni += len_B
        else:
            ni += 1

    print(f"#{num+1} {len_A - (cnt*(len_B - 1))}")