import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    cards_1 = []
    cards_2 = []
    
    # 일단 플레이어 1, 플레이어 2 순서대로 각각 카드 3장까지 받아봄
    # 카드 받는 형식: cards 안의 맨 앞 숫자 가져가고 그 숫자 pop 하여 맨 앞 숫자 계속 바꿔주는 형식
    tmp = 0
    for i in range(3):
        tmp = cards[0]
        cards_1.append(tmp)
        cards_1.sort()
        # 3장 받았을 때 run 이나 triplet 인지 확인
        if i == 2:
            if ((cards_1[i] == cards_1[i-1] and cards_1[i-1] == cards_1[i-2])
                    or (cards_1[i-2] +1 == cards_1[i-1] and cards_1[i-1] +1 == cards_1[i])):
                print(f"#{tc} 1")
                break
        cards.pop(0)
        
        
        tmp = cards[0]
        cards_2.append(tmp)
        cards_2.sort()
        # 두 번째 플레이어도 마찬가지로 3장 되었을 때 확인
        if i == 2:
            if ((cards_2[i] == cards_2[i-1] and cards_2[i-1] == cards_2[i-2])
                    or (cards_2[i-2] +1 == cards_2[i-1] and cards_2[i-1] +1 == cards_2[i])):
                print(f"#{tc} 2")
                break
        cards.pop(0)

    # 중요!!! 3장씩 해 봤는데 결판이 나지 않았다면 나머지 카드들 분배하면서 진행
    # 카드 받는 형식은 같음
    # ps: 앞에 꺼랑 무관하게(else 안에서 말고) 새롭게 for 문 돌았다가 계속 답이 틀려서 당황...
    else:
        for _ in range(3):
            tmp = cards[0]
            cards_1.append(tmp)
            cards_1.sort()
            # triplet 확인
            if cards_1.count(tmp) >= 3:
                print(f"#{tc} 1")
                break
            # run 확인1 --> 일반적인 경우: 6 기준으로 456 / 567 / 678 되는 경우 탐색
            # 이런 식으로 하면 무조건 index 벗어나기에 IndexError 발생하면 pass
            try:
                if ((cards_1[cards_1.index(tmp) -2] +1 == cards_1[cards_1.index(tmp) -1] and cards_1[cards_1.index(tmp) -1] +1 == cards_1[cards_1.index(tmp)])
                        or (cards_1[cards_1.index(tmp) -1] +1 == cards_1[cards_1.index(tmp)] and cards_1[cards_1.index(tmp)] +1 == cards_1[cards_1.index(tmp) +1])
                        or (cards_1[cards_1.index(tmp)] +1 == cards_1[cards_1.index(tmp) +1] and cards_1[cards_1.index(tmp) +1] +1 == cards_1[cards_1.index(tmp) +2])):
                    print(f"#{tc} 1")
                    break
            except IndexError:
                pass
            # run 확인2 --> 특별한 경우: 6 기준으로 4456 / 4556 / 5567 / 5677 / 6778 / 6788 되는 경우 탐색
            try:
                if ((cards_1[cards_1.index(tmp) - 3] + 1 == cards_1[cards_1.index(tmp) - 1] and cards_1[cards_1.index(tmp) - 1] + 1 == cards_1[cards_1.index(tmp)])
                        or (cards_1[cards_1.index(tmp) - 1] + 1 == cards_1[cards_1.index(tmp)] and cards_1[cards_1.index(tmp)] + 1 == cards_1[cards_1.index(tmp) + 1])
                        or (cards_1[cards_1.index(tmp)] + 1 == cards_1[cards_1.index(tmp) + 1] and cards_1[cards_1.index(tmp) + 1] + 1 == cards_1[cards_1.index(tmp) + 3])):
                    print(f"#{tc} 1")
                    break
            except IndexError:
                pass
            # run 확인3 --> 특별한 경우: 6 기준으로 44556 / 55677 / 67788 되는 경우 탐색
            try:
                if ((cards_1[cards_1.index(tmp) - 4] + 1 == cards_1[cards_1.index(tmp) - 2] and cards_1[cards_1.index(tmp) - 2] + 1 == cards_1[cards_1.index(tmp)])
                        or (cards_1[cards_1.index(tmp) - 2] + 1 == cards_1[cards_1.index(tmp)] and cards_1[cards_1.index(tmp)] + 1 == cards_1[cards_1.index(tmp) + 2])
                        or (cards_1[cards_1.index(tmp)] + 1 == cards_1[cards_1.index(tmp) + 2] and cards_1[cards_1.index(tmp) + 2] + 1 == cards_1[cards_1.index(tmp) + 4])):
                    print(f"#{tc} 1")
                    break
            except IndexError:
                pass
            cards.pop(0)

            # 두 번째 플레이어도 마찬가지로 진행: 위의 코드 길이가 길어서 '뭐야 쟤는 카드 다 가져갔나' 할 수 있지만
            # for 문 안에 있으니 한 장씩 받으면서 하고 있음
            tmp = cards[0]
            cards_2.append(tmp)
            cards_2.sort()

            if cards_2.count(tmp) >= 3:
                print(f"#{tc} 2")
                break
            try:
                if ((cards_2[cards_2.index(tmp) -2] +1 == cards_2[cards_2.index(tmp) -1] and cards_2[cards_2.index(tmp) -1] +1 == cards_2[cards_2.index(tmp)])
                        or (cards_2[cards_2.index(tmp) -1] +1 == cards_2[cards_2.index(tmp)] and cards_2[cards_2.index(tmp)] +1 == cards_2[cards_2.index(tmp) +1])
                        or (cards_2[cards_2.index(tmp)] +1 == cards_2[cards_2.index(tmp) +1] and cards_2[cards_2.index(tmp) +1] +1 == cards_2[cards_2.index(tmp) +2])):
                    print(f"#{tc} 2")
                    break
            except IndexError:
                pass
            # 특별한 경우: 6 기준으로 4456 / 4556 / 5567 / 5677 / 6778 / 6788 되는 경우 탐색
            try:
                if ((cards_2[cards_2.index(tmp) - 3] + 1 == cards_2[cards_2.index(tmp) - 1] and cards_2[cards_2.index(tmp) - 1] + 1 == cards_2[cards_2.index(tmp)])
                        or (cards_2[cards_2.index(tmp) - 1] + 1 == cards_2[cards_2.index(tmp)] and cards_2[cards_2.index(tmp)] + 1 == cards_2[cards_2.index(tmp) + 1])
                        or (cards_2[cards_2.index(tmp)] + 1 == cards_2[cards_2.index(tmp) + 1] and cards_2[cards_2.index(tmp) + 1] + 1 == cards_2[cards_2.index(tmp) + 3])):
                    print(f"#{tc} 2")
                    break
            except IndexError:
                pass
            # 특별한 경우: 6 기준으로 44556 / 55677 / 67788 되는 경우 탐색
            try:
                if ((cards_2[cards_2.index(tmp) - 4] + 1 == cards_2[cards_2.index(tmp) - 2] and cards_2[cards_2.index(tmp) - 2] + 1 == cards_2[cards_2.index(tmp)])
                        or (cards_2[cards_2.index(tmp) - 2] + 1 == cards_2[cards_2.index(tmp)] and cards_2[cards_2.index(tmp)] + 1 == cards_2[cards_2.index(tmp) + 2])
                        or (cards_2[cards_2.index(tmp)] + 1 == cards_2[cards_2.index(tmp) + 2] and cards_2[cards_2.index(tmp) + 2] + 1 == cards_2[cards_2.index(tmp) + 4])):
                    print(f"#{tc} 2")
                    break
            except IndexError:
                pass
            cards.pop(0)
        
        # 카드 다 가져갔는데(for문 다 돌았는데) 승부가 안 났다면 0 출력
        else:
            print(f"#{tc} 0")




