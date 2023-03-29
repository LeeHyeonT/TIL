import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
ans = 0
for _ in range(n):
    word = input()
    dict = {}
    for i in range(len(word)):
        if i == 0:
            dict[word[i]] = 1
        else:
            if word[i-1] == word[i]:
                dict[word[i]] += 1
            else:
                if word[i] in dict:
                    break
                else:
                    dict[word[i]] = 1

    else:
        ans += 1
        
print(ans)