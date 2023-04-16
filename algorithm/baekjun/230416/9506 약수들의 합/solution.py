import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == -1:
        break
    else:
        num_list = []
        for i in range(1, n):
            if n % i == 0:
                num_list.append(i)
        if sum(num_list) == n:
            print(f'{n} =', end=' ', sep='')
            for j in range(len(num_list)-1):
                print(f'{num_list[j]} +', end=' ', sep='')
            print(num_list[len(num_list)-1])
        else:
            print(f'{n} is NOT perfect.')
            
'''
정확히는, sep을 명시적으로 인자로 주지 않으면 ' '이 기본값으로 지정되어 있습니다. 그렇기 때문에 sep을 인자로 주지 않을 시에 인자 사이가 공백으로 구분이 됩니다. 
하지만 이 코드에서는 이 sep을 빈 문자열로 명시해서 주었기 때문에, 인자 사이에 아무것도 출력이 되지 않습니다.
해당 문장에서 출력해야 하는 것은 '(n의 값) = (j_num의 값)'인데, 이미 두 번째 인자에서 '=' 문자의 앞뒤로 공백을 넣어서 줬기 때문에 추가적인 공백이 필요하지 않습니다. 
그렇기 때문에 sep을 빈 문자열로 명시해준 것입니다. 만일 sep=''을 넣지 않으면 sep이 공백 하나가 되기 때문에, 불필요하게 인자들 사이에 공백이 하나씩 더 들어갑니다.

예제 출력에서 첫 줄에 나와야 하는 것
6 = 1 + 2 + 3
sep=''을 안 넣으면 출력되는 것
6  =  1 + 2 + 3
'''