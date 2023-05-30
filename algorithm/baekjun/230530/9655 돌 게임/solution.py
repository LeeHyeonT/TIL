import sys
sys.stdin  = open('input.txt', encoding='UTF-8')

n = int(input())
if n % 2:
    print('SK')
else:
    print('CY')
    
    
'''
문제 본질만 잘 파악한다면 엄청 쉬운 문제
돌을 1개 혹은 3개만 가져갈 수 있기에 전형적인 짝수홀수 문제로 둔갑!
이걸 알아보는 데에 5분 이상 쓰지 않아서 다행....
'''