import sys
sys.stdin = open('input.txt', encoding='UTF-8')

while True:
    try:
        message = input()
        print(message)
    except EOFError:
        exit()