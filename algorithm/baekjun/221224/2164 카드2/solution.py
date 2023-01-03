import sys
sys.stdin = open('input.txt', encoding='UTF-8')
'''
정신승리 해야지!
이 코드는 실패한 코드!
'''
# N = int(input())
# array = []
# for i in range(0, N+1):
#     array.append(i)
# start_index = 1
# end_index = N
# count = 1
# while True:
#     if start_index == end_index:
#         print(array[start_index])
#         break
#     start_index += (2 ** (count-1))
#     if start_index > N: 
#         count += 1
#         start_index = 2 ** (count-1)
#     end_index = start_index
#     start_index += (2 ** (count-1))
#     if start_index > N:
#         count += 1
#         start_index =  2 ** (count-1)
#     print(start_index, end_index)

a = int(input())
b = 2
while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if b >= a:
        print((a - (b // 2)) * 2)
        break
    
'''
recursion error 발생 코드
'''
# def queue_function(array):
#     if len(array) == 1:
#         print(array[0])
#         return
#     array.pop(0)
#     if len(array) == 1:
#         print(array[0])
#         return
#     target_number = array.pop(0)
#     array.append(target_number)
#     if len(array) == 1:
#         print(array[0])
#         return
#     queue_function(array)

# queue_function(start_array)

'''
시간 초과 코드
'''
# while True:
#     if len(start_array) == 1:
#         print(start_array[0])
#         break
#     start_array.pop(0)
#     if len(start_array) == 1:
#         print(start_array[0])
#         break
#     target_number = start_array.pop(0)
#     start_array.append(target_number)