import sys
sys.stdin = open('input.txt', encoding='UTF-8')
def calculate_prize(dice_results):
    count_dict = {}
    for num in dice_results:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_count = max(count_dict.values())
    if max_count == 4:
        return 50000 + next(num for num, count in count_dict.items() if count == 4) * 5000
    elif max_count == 3:
        return 10000 + next(num for num, count in count_dict.items() if count == 3) * 1000
    elif max_count == 2:
        pairs = [num for num, count in count_dict.items() if count == 2]
        if len(pairs) == 2:
            return 2000 + pairs[0] * 500 + pairs[1] * 500
        else:
            return 1000 + pairs[0] * 100
    else:
        return max(dice_results) * 100

N = int(input())
max_prize = 0
for _ in range(N):
    dice_results = list(map(int, input().split()))
    prize = calculate_prize(dice_results)
    if prize > max_prize:
        max_prize = prize

print(max_prize)