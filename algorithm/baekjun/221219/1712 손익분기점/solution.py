import sys
sys.stdin = open('input.txt', encoding='UTF-8')

must, produce, price = map(int, input().split())

# '''
# 이렇게 하면 시간초과가 나온다!
# 그럼 어떻게 하는 것이 좋을까?
# '''
# price_A = 0
# price_B = 0
# count = 1
# while True:
#     if produce >= price:
#         print(-1)
#         break
#     price_A = must + produce * count
#     price_B = price * count
#     if price_B > price_A:
#         print(count)
#         break
#     count += 1

'''
must 를 price - produce 로 나눠 그 몫을 구하면 된다!
'''
number_A = price - produce
count = 1
if number_A <= 0:
    print(-1)
else:
    count += must // number_A
    print(count)
