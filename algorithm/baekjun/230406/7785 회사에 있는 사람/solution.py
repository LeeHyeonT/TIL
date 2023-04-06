import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
n = int(input())
log = {}

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        log[name] = True   # 입장 상태를 True로 저장
    else:
        log[name] = False  # 입장 상태를 False로 저장

present = []
for name, status in log.items():
    if status:  # 입장 상태가 True(회사에 있다)이면
        present.append(name)

present.sort(reverse=True)  # 사전 순의 역순으로 정렬
for name in present:
    print(name)