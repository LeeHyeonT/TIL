import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

N = int(input())
time_list = list(map(int, input().split()))

'''
문제 조건이 난이도가 낮아 허술한 편이여서 sort 하고 더해주기만 해도 무난하게 맞는 문제
하지만 문제 조건이 까다로워진다면?
일단 문제를 풀기 위해서는 sort 는 필수적
내장되어있는 sort 를 사용한다면 시간복잡도는 O(nlogn): 그리 나쁜 복잡도는 아님
'''
time_list.sort()

time = 0
index = 0
while True:
    if index == N:
        break
    for i in range(0, index+1):
        time += time_list[i]
    index += 1
print(time)
