import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp = [0] * N
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    print(dp[N-1])

'''
dp 하면서 느끼는 것 중 하나가 반복하는 횟수는 같은데 왜 메모리며 시간을 적게 먹는 것인가....
dp에서의 반복은 단순 for문을 돌아 range 값을 이용하여 array의 index를 탐색하는 시간이 대부분
다른 반복의 경우 반복을 돌며 다른 작업 자체를 다시 시행함 
여기서 메모리와 시간의 차이가 발생하는 것 같음
'''