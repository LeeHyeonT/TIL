import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

n = int(input().rstrip())
storage = {}
tmp = 0
ans = 0
while True:
    if tmp == n:
        for i in storage.values():
            ans += i
        break
    a = input().rstrip()
    if a == 'ENTER' and tmp != 0:
        for i in storage.values():
            ans += i
        storage.clear()
    else:
        if a != 'ENTER' and a not in storage:
            storage[a] = 1
        else:
            pass
    tmp += 1
    
print(ans)

'''
다른 풀이들과 비교했을 때 시간 소요가 약간 더 되지만(10ms) 메모리 사용량이 더 적기에 (3000~4000KB) 괜찮은 풀이라고 할 수 있을듯!
'''