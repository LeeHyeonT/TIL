import sys
sys.stdin = open('input.txt', encoding='UTF-8')

hour, min = map(int, input().split())
progress = int(input())

answer_min = min + progress
count = 0
if answer_min >= 60:
    count = answer_min // 60
    answer_min = answer_min % 60
    hour += count
    
answer_hour = hour
if hour >= 24:
    answer_hour = hour % 24

print(answer_hour, answer_min)