import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n, m = map(int, input().split())
deque = [0] * n
nums = list(map(int, input().split()))
c_value = 1
for num in nums:
    deque[num-1] = c_value
    c_value += 1
else:
    c_value = 1

cnt = 0
while True:
    if m == 0:
        break

    if deque[0] == c_value:
        deque.pop(0)
        m -= 1
        c_value += 1
    else:
        if deque.index(c_value) >= len(deque) / 2:
            a = deque.pop()
            deque.reverse()
            deque.append(a)
            deque.reverse()
          
            cnt += 1
        else:
            a = deque.pop(0)
            deque.append(a)
          
            cnt += 1
print(cnt)


'''
원래 24번 줄의
 if deque.index(c_value) >= len(deque) / 2:
 에서 
 deque.index(c_value) + 1 
 값을 줬는데 이러면 안 되는 것이었다...!
 이미 deque 구성할 때 값 주는 것은 끝났기에 deque array 그 자체의 index로 비교를 해야지
 저기서도 보정한답시고 +1 을 하면 안 되는 것이다
'''