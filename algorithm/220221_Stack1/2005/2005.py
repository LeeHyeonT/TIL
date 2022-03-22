import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# 6. pascal 이라는 함수 만들기
def pascal(n):
    # memo 값을 전역에서 쓰기 위해 전역 변수로 설정
    global memo
    # n 이 1, 2 인 경우 규칙을 주기 어렵다고 판단하여 따로 설정
    if n == 1:
        memo = [1]
        return memo
    elif n == 2:
        memo = [1, 1]
        return memo
    # n이 3 이상일 때부터 그 전의 memo 값을 이용하여 파스칼 삼각형 작성
    else:
        if n >= 3 and len(memo) <= n:
            # memo 에 들어갈 tmp 를 copy
            tmp = memo[:]
            # 맨 앞자리 제외하고 다 제거함, memo = [1] 로 해도 될듯?
            for _ in range(n-2):
                memo.pop()
            # 두 번째 자리부터 아까 copy 한 tmp 이용: pascal 삼각형 법칙 이용하여 값 더함 
            for i in range(1, n-1):
                memo.append(tmp[i] + tmp[i-1])
            # 맨 마지막 자리는 항상 1이므로 1 더해줌
            memo.append(1)
        return memo
    
# 1. test case 갯수 입력받음
T = int(input())
# 2. test case 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    # 3. test case 나올 때마다 numbering 한 번씩 출력, end 는 enter 로 줌
    print(f"#{tc}", end= "\n")
    # 4. 1 ~ n 까지 반복
    for j in range(1, n+1):
        # 5. pascal 이라는 함수를 만들어 사용 예정
        print(*pascal(j))