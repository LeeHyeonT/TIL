import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input()) # 배열의 크기 N을 입력받음
k = int(input()) # k를 입력받음

# 이진 탐색으로 k번째 수 찾기
left, right = 1, k # left: k 이하의 수가 몇 개 있는지 계산하기 위한 변수
while left <= right:
    mid = (left + right) // 2 # 중간값
    count = 0 # mid 이하인 수의 개수
    for i in range(1, n+1):
        count += min(mid // i, n) # mid 이하인 수의 개수를 계산하여 누적
    if count >= k:
        answer = mid # mid가 k번째 수 이상인 경우
        right = mid - 1 # mid를 줄여서 더 작은 값을 찾음
    else:
        left = mid + 1 # mid를 늘려서 더 큰 값을 찾음

# k번째 수 출력
print(answer)

'''
index 에 함몰되지 않는 아이디어가 필요한 문제
이분 탐색으로 풀어야하는 것 까지는 알려줬으나 어떻게 풀어나가야할지에 대해 생각하는 것은 오롯이 푸는 사람의 몫
이 문제는 left 를 N*N 이 아닌 K 로 접근하여 손쉽게 문제를 풀어나갔다.
가장 중요한 코드는
for i in range(1, n+1):
    count += min(mid // i, n)
이 부분일 것이다. 아이디어가 없으면 떠올릴 수 없는 코드.
'''