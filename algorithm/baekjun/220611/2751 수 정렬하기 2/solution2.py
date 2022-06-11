import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def quick_sort(array, start, end):
    if start >= end: 
        return
    pivot = start 
    left = start + 1
    right = end
    while(left <= right):
        
        while(left <= end and array[left] <= array[pivot]):
            left += 1
  
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): 
            array[right], array[pivot] = array[pivot], array[right]
        else: 
            array[left], array[right] = array[right], array[left]
 
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


N = int(input())
num_arr = []

for _ in range(N):
    num = int(input())
    num_arr.append(num)

quick_sort(num_arr, 0, len(num_arr) - 1)

for a in num_arr:
    print(a)

# 이거로도 안 풀린다...
# 이유는 잘 모르겠다 RecursionError 뜨는데 어디서 계속 삥삥 도는지....