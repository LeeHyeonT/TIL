import sys
sys.stdin = open('input.txt', encoding='UTF-8')

num_array = []
for _ in range(5):
    num_array.append(int(input()))
    
print(round(sum(num_array) / len(num_array), None))

num_array.sort()
print(num_array[len(num_array) //  2])
        