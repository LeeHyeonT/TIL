import sys
sys.stdin = open('input.txt', encoding='UTF-8')

dice_list = list(map(int, input().split()))
dice_list.sort()
if dice_list[0] != dice_list[1] and dice_list[1] != dice_list[2] and dice_list[2] != dice_list[0]:
    print(max(dice_list) * 100)
elif (dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2]) and dice_list[2] != dice_list[0]:
    print(1000 + dice_list[1] * 100)
else:
    print(10000 + dice_list[1] * 1000)