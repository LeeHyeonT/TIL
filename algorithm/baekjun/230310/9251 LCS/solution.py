import sys
sys.stdin = open('input.txt', encoding='UTF-8')

chr1 = input()
chr2 = input()
dp = [[0] * (len(chr2) + 1) for _ in range(len(chr1) + 1)]

for i in range(1, len(chr1) + 1):
    for j in range(1, len(chr2) + 1):
        if chr1[i-1] == chr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(max(dp)))

'''
두 문자열의 길이가 같다는 조건이 없으므로 dp 배열을 1차원 배열이 아닌 2차원 배열로 진행해야한다!
'''