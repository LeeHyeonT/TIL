import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
group = []
member = list(([] for _ in range(n)))

for i in range(n):
    team = input().rstrip()
    group.append(team)
    num = int(input().rstrip())
    for _ in range(num):
        name = input().rstrip()
        member[i].append(name)
for _ in range(m):
    quiz = input().rstrip()
    quiz_num = int(input().rstrip())
    if quiz_num == 1:
        for j in range(n):
            if quiz in member[j]:
                print(group[j])
                break
    else:
        for k in range(n):
            if quiz == group[k]:
                member[k].sort()
                print('\n'.join(member[k]))
                break