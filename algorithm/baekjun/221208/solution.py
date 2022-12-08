# import sys
# sys.stdin = open('input.txt', encoding='UTF-8')
# input = sys.stdin.readline

# character = input()
# num = int(input())
# range_lists = []
# for _ in range(num):
#     line = list(map(str, input().split()))
#     range_lists.append(line)
# print(range_lists)
# accum_list = [0] * len(character)
# alphabet_sum = []
# for i  in range(1, 27):
#     if 
# for i  in range(len(range_lists)):

# # for i in range(len(character)):
# #     if character[i] == target:
# #         accum_list[i] += 1

# # print(accum_list)
# # for range_list in range_lists:
# #     print(accum_list[range_list[0]: range_list[1]+1])
# #     print(sum(accum_list[range_list[0]: range_list[1]+1]))


'''
알파벳 소문자까지는 생각했는데
그 이후 방법은 잘 떠오르지 않았다....
그 소문자를 이중 list 로 이용해야하는 거인지는 잘 인지가 되지 않았던 상태
'''
sys.stdin = open('input.txt', encoding='UTF-8')
import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]

arr[0][ord(s[0])-97] = 1
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1

for _ in range(int(input())):
    c,start,end = list(input().split())
    start,end = map(int,[start,end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])
   