import sys
sys.stdin = open('input.txt', 'r')

# 순열
def make_perm(perm, lst, number):
    if len(perm) == r:
        perm.sort()
        visited.append(perm)
        print(visited)
        print(perm)
        if perm not in visited:
            if (perm[0] == perm[1] and perm[1] == perm[2]) or (perm[1] - 1 == perm[0] and perm[1] + 1 == perm[2]):
                print(f"#{tc} {number}")
                print(perm)
                return

    for i in lst:
        if i not in perm:
            perm.append(i)
            make_perm(perm, lst, number)
            perm.pop()

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    cards_1 = []
    cards_2 = []
    r = 3
    tmp = 0
    visited = []

    # 일단 3개까지 넣어봄
    for i in range(3):
        tmp = cards[0]
        cards_1.append(tmp)
        cards.pop(0)
        if i == 2:
            make_perm([], cards_1, 1)

        tmp = cards[0]
        cards_2.append(tmp)
        cards.pop(0)
        if i == 2:
            make_perm([], cards_2, 2)

    # 나머지 것들도 넣어봄
    for _ in range(3):
        tmp = cards[0]
        cards_1.append(tmp)
        cards.pop(0)
        make_perm([], cards_1, 1)

        tmp = cards[0]
        cards_2.append(tmp)
        cards.pop(0)
        make_perm([], cards_2, 2)

    else:
        print(f"#{tc} 0")