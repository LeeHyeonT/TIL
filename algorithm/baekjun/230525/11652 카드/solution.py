import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
N = int(input())  # 카드의 개수 입력 받기
cards = {}  # 딕셔너리 생성

# 카드의 개수만큼 반복하면서 딕셔너리에 정수 개수 기록
for _ in range(N):
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

# 딕셔너리에서 가장 많이 나온 정수 찾기
max_count = max(cards.values())
max_nums = [num for num, count in cards.items() if count == max_count]
max_nums.sort()

print(max_nums[0])  # 가장 작은 정수 출력

'''
dictionary 구조 활용법을 좀 더 확고히 하자
chatgpt의 도움으로 풀긴 했음...!
'''