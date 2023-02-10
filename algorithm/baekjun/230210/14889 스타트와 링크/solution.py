import sys
sys.stdin = open('input.txt', encoding='UTF-8')

from itertools import permutations

N = int(input())
player_array = list(list(map(int, input().split())) for _ in range(N))

start_team = []
link_team = []
gap = 10000


def TeamMaking(index):
    global gap
    if len(start_team) == N // 2:
        for j in range(N):
            if j  not in start_team:
                link_team.append(j)
        
        start_perm = list(permutations(start_team, 2))
        link_perm = list(permutations(link_team, 2))
        start_score = 0
        link_score = 0

        for sp in start_perm:
            start_score += player_array[sp[0]][sp[1]]
        for lp in link_perm:
            link_score += player_array[lp[0]][lp[1]]
        
        if gap > abs(start_score - link_score):
            gap = abs(start_score - link_score)
            if gap == 0:
                print(gap)
                exit(0)
        link_team.clear()
        return

    else:
        for i in range(N):
            if i in start_team: 
                continue
            if len(start_team)>0 and start_team[len(start_team)-1]> i :
                 continue
            start_team.append(i)
            TeamMaking(index)
            start_team.pop()

TeamMaking(0)
print(gap)

'''
쉬워보였지만 스스로의 힘으로 (일단) 못 푼 문제...
이 문제의 task가
1) N 명을 두 그룹으로 나누기
2) 두 그룹으로 나뉜 사람들을 크기 2짜리 순열로 표현하기
3) 표현한 사람들의 값을 더해 비교하기
인데 1) 번을 하는 과정에서 번거로움이 발생했다
처음에는 start_team 에 모든 선수 넣어놓고 start_team 에서 pop 한 선수를 link_team 에 append 하는 방식으로 선수를 분배하고
함수 변수에 start_team, link_team 을 받아 진행하려고했으나 뜻대로 잘 되지 않음...
결국 start_team, link_team 둘 다 비워놓고 index 활용으로 넘어옴
이 때 43번 줄의 
start_team[len(start_team)-1]> i 
이 조건이 중요한 것 같음
player들을 오름차순으로 나타내도록 유도하는 녀석
'''


