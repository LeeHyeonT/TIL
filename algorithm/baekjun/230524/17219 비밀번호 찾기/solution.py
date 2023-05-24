import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
storage = {}
for _ in range(n):
    site, password = map(str, input().rstrip().split())
    storage[site] = password
for _ in range(m):
    site_2 = input().rstrip()
    print(storage[site_2])
    
'''
python 의 경우 dictionary 자료 구조만 사용할 줄 안다면 쉽게 풀 수 있는 문제
dictionary를 사용하지 않는다면 list를 활용
'''