import sys
sys.stdin = open('input.txt', encoding="UTF-8")
from datetime import datetime

n = int(input())  # 학생 수 입력
students = []  # 학생 정보를 저장할 리스트

# 학생 정보 입력
for _ in range(n):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    students.append((name, datetime(year, month, day)))

# 가장 나이가 적은 사람과 가장 많은 사람 찾기
youngest = max(students, key=lambda x: x[1])[0]
oldest = min(students, key=lambda x: x[1])[0]

# 결과 출력
print(youngest)
print(oldest)

'''
datetime 내장함수를 활용하여 정렬을 3번해야할 것을 1번으로 줄일 수 있다.
'''