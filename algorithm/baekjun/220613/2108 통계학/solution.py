import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def sansul(lst):
    res = 0
    for i in lst:
        res += i
    res = round(res / len(lst))
    return print(res)

def middle(lst):
    return print(lst[len(lst)//2])  

def often(lst):
    count = [0] * 8001
    for i in lst:
        if i != 0:
            count[4000+i] += 1
        else:
            count[4000] += 1
    
    count_idx = []
    for j in range(len(count)):
        if count[j] >= max(count):
            count_idx.append(j)
  
    if len(count_idx) > 1:
        return print(count_idx[1] - 4000)
        
    else:
        return print(count_idx[0] - 4000)

def bigsmall(lst):
    return print(lst[-1] - lst[0])

N = int(input())
num_arr = []
for _ in range(N):
    num = int(input())
    num_arr.append(num)

num_arr.sort()

sansul(num_arr)
middle(num_arr)
often(num_arr)
bigsmall(num_arr)

