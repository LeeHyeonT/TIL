import sys
sys.stdin= open('input.txt', encoding='UTF-8')

# 연두의 영어 이름 입력
name = input().strip()

# 팀 이름 후보의 개수 입력
N = int(input())

# 팀 이름 후보들을 리스트에 저장
team_names = []
for _ in range(N):
    team_name = input().strip()
    team_names.append(team_name)

# 주어진 공식에 따라 우승 확률 계산 함수
def calculate_probability(name, team_name):
    L = name.count('L') + team_name.count('L')
    O = name.count('O') + team_name.count('O')
    V = name.count('V') + team_name.count('V')
    E = name.count('E') + team_name.count('E')
    
    probability = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    return probability

# 가장 높은 우승 확률을 가진 팀 이름 찾기
max_probability = -1
best_team_name = ""
for team_name in team_names:
    probability = calculate_probability(name, team_name)
    if probability > max_probability:
        max_probability = probability
        best_team_name = team_name
    elif probability == max_probability and team_name < best_team_name:
        best_team_name = team_name

# 결과 출력
print(best_team_name)
