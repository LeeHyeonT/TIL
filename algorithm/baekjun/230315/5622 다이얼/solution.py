import sys
sys.stdin = open('input.txt', encoding='UTF-8')

word = input()
ans = 0
for i in word:
    if i == 'S' or i == 'V' or i == 'Y' or i == 'Z':
        num = (ord(i) - 65) // 3 + 2
    else:
        num = (ord(i) - 62) // 3 + 2
    ans += num
print(ans)