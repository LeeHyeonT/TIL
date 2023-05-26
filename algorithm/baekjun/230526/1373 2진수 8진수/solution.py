import sys
sys.stdin = open('input.txt', encoding='UTF-8')

binary = input()  # 2진수 입력

# 입력된 2진수를 10진수로 변환
decimal = int(binary, 2)

# 10진수를 8진수로 변환
octal = oct(decimal)

# 변환된 8진수에서 '0o' 접두사 제거
octal = octal[2:]

print(octal)  # 결과 출력

'''
내장함수만 활용하더라도 100만자리 이하의 2진수는 8진수로 무난하게 변환 가능하다.
'''

