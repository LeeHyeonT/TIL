import sys
sys.stdin = open('input.txt', encoding='UTF-8')

word = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_index = [-1] * 26

for i in range(len(word)):
    for j in range(len(alphabet)):
        if word[i] == alphabet[j]:
            if alphabet_index[j] == -1:
                alphabet_index[j] = i
            else:
                pass

for index in alphabet_index:
    print(index, end=' ')

'''
알파벳 갯수는 26개이다
이렇게 간단한 문제는 dictionary 사옹 시 시간이 더 오래 걸린다
alphabet을 문자열로 abcd... 하는 거나 나처럼 list에 저장해서 쓰는 거나 시간 차이는 없다
'''