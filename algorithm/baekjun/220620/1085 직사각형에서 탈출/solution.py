import sys
sys.stdin = open('input.txt', encoding='UTF-8')

x,y,w,h = map(int, input().split())

print(min(abs(x-w), abs(y-h), x, y))

# 내부 함수를 이용하여 적은 코드로 푼 모습
# min을 안 쓰더라도 대소관계 이용하여 풀 줄 알아야!