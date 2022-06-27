import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N, M = map(int, input().split())


# 진짜 팩토리얼로 구해서 문제를 해결하게 되면 시간초과 발생
# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)

# 생각하닥 안 나서 참고했다...
# 2,5 갯수 찾는 건 비슷한 개념이지만 팩토리얼 계산을 하지 않고도 가능
# 몫을 이용하여 계산