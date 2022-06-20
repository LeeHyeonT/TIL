import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N , M = map(int, input().split())

pokemon_dict = dict()

for i in range(1, N+1):
    a = input()
    pokemon_dict[a] = i
    pokemon_dict[i] = a

print(pokemon_dict)

for _ in range(M):
    b = input()
    try:
        print(pokemon_dict[int(b)])
    except ValueError:
        print(pokemon_dict[f'{b}'])
    
    # dictionary 는 신이다!!