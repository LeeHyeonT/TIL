import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline
N = int(input().rstrip())  # 카드의 개수 입력 받기
cards = []  # 리스트 생성

# 카드의 개수만큼 반복하면서 리스트에 정수 기록
for _ in range(N):
    num = int(input().rstrip())
    cards.append(num)

# 리스트에서 가장 많이 나온 정수 찾기
max_num = max(cards, key=cards.count)
cards.sort()

print(max_num)  # 가장 작은 정수 출력


'''
list 를 활용하여 문제를 풀어보고자했지만 시간 초과가 발생한다
이는 데이터를 다루는 자료 구조 간 효율성 차이 때문으로, 단순 숫자 갯수 비교의 경우 dictionary 가 list 보다 보다 빠른 순회 속도를 자랑한다.
'''