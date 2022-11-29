import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(T):
    student_score_list = list(map(int, input().split()))
    student = student_score_list.pop(0)
    score_list = student_score_list[:]

    # 평균 구하기
    score_avg = sum(score_list) / student

    # 평균 초과인 사람 수 구하기
    upper_avg = 0
    for score in score_list:
        if score > score_avg:
            upper_avg += 1

    # 답 도출하기
    # 소숫점 제한하는 방법 잘 알아두자
    upper_avg_percent = f'{(upper_avg / student * 100) :.3f}'
    print(f'{upper_avg_percent}%')
