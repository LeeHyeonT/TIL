import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def count_ways(N):
    # 동적 계획법을 위한 배열 초기화
    dp = [[0] * 3 for _ in range(N+1)]
    
    # 초기값 설정
    dp[1][0] = dp[1][1] = dp[1][2] = 1
    
    for i in range(2, N+1):
        # 현재 단계에서 첫 번째 칸에 사자를 배치하는 경우의 수
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
        
        # 현재 단계에서 두 번째 칸에 사자를 배치하는 경우의 수
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
        
        # 현재 단계에서 어느 칸에도 사자를 배치하지 않는 경우의 수
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
    
    # 마지막 단계에서 사자를 배치하는 경우의 수의 합을 구함
    total = (dp[N][0] + dp[N][1] + dp[N][2]) % 9901
    
    return total

# 입력 받기
N = int(input())

# 사자를 배치하는 경우의 수 계산
result = count_ways(N)

# 결과 출력
print(result)

'''
chatgpt3.5 와의 혈투 끝에 얻어낸 코드.
노력하면 정답인 코드를 얻을 수 있다...
이 문제에서는 해당 공간에 사자가 놓여있는지 안 놓여있는지에 대한 정보가 중요!
이전 단계의 그 정보를 다음 단계에 활용하기 때문
'''