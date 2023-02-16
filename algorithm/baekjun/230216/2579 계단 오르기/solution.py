import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
stair_score = []
dp = [0] * N
for _ in range(N):
    stair_score.append(int(input()))

if len(stair_score)<=2:
    print(sum(stair_score))
else: 
    dp[0] = stair_score[0] 
    dp[1] = stair_score[0]+stair_score[1] 
    for i in range(2,N):
        dp[i] = max(dp[i-3] + stair_score[i-1] + stair_score[i], dp[i-2] + stair_score[i])
    print(dp[-1])


'''
혼자 힘으로 풀지 못한 문제...
dp[i]=max(dp[i-3] + stair_score[i-1] + stair_score[i], dp[i-2] + stair_score[i])
이 코드에서 연속된 세 계단 이상 안 걷는 것까지 포함되어있다...
이런 점화식을 잘 생각하려면 더 숙달되어야 하겠지
ps. chatGPT 를 이용하여 문제를 풀어보려고 했다

def maxPoints(stairPoints):
  max_points = 0

  for i in range(len(stairPoints)):
    # Calculate the maximum number of points for taking one step
    if i+1 < len(stairPoints):
      max_points_one_step = stairPoints[i] + stairPoints[i+1]
    else:
      max_points_one_step = stairPoints[i]
    
    # Calculate the maximum number of points for taking two steps
    if i+2 < len(stairPoints):
      max_points_two_steps = stairPoints[i] + stairPoints[i+1] + stairPoints[i+2]
    else:
      max_points_two_steps = stairPoints[i]
    
    # Get the maximum of the two points
    max_points_current = max(max_points_one_step, max_points_two_steps)
    
    # Update the maximum points
    max_points = max(max_points, max_points_current)

  return max_points

이런 코드를 짜줬는데 내 설명이 좀 부족했는지 완벽한 코드가 나오지는 않았다
하지만 대강 설명해줘도 이렇게 코드를 쭉 뽑아내는 것을 보니 인류의 종말이 가까워지지 않았나...하는 생각이 든다
'''