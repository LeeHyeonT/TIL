import sys
sys.stdin = open('input.txt',encoding='UTF-8')

N = int(input())
normal_list = list(map(int, input().split()))
best_score = max(normal_list)
new_list = []
for score in normal_list:
    new_list.append(score / best_score * 100)
print(sum(new_list) / len(new_list))


'''
상대오차가 10^-2 이하면 정답이라 약간 긴장했지만 정답처리 잘 되었다.
'''