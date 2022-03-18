import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 직관적인 방법
    for i in range(1, 10**6 + 1):
        if i*i*i == N:
            print(f"#{tc} {i}")
            break
    else:
        print(f"#{tc} -1")

    # 세제곱근 이용
    