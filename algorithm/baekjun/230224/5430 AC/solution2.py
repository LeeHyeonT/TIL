from collections import deque
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 테스트 케이스의 개수 입력 받기
t = int(input())

for _ in range(t):
    # 수행할 함수 입력 받기
    p = input()
    # 배열의 길이 입력 받기
    n = int(input())
    # 배열 입력 받기
    a = input()
    if a == '[]':
        arr = deque()
    else:
        arr = deque(map(int, a[1:-1].split(',')))

    
    # 뒤집기 횟수 계산을 위한 변수
    reverse_count = 0
    # 에러 여부를 체크하기 위한 변수
    error = False
    
    # 함수 하나씩 순회하며 수행
    for func in p:
        # 뒤집기 함수일 경우 뒤집기 횟수 증가
        if func == 'R':
            reverse_count += 1
        # 버리기 함수일 경우 배열의 길이 체크 후 첫 번째 값 버리기
        else:
            if len(arr) == 0:
                error = True
                break
            if reverse_count % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    
    # 에러가 발생한 경우 "error" 출력
    if error:
        print("error")
    else:
        # 뒤집기 횟수에 따라 배열 뒤집기
        if reverse_count % 2 == 1:
            arr.reverse()
        # 결과 출력
        print("[", end='')
        for i in range(len(arr)):
            print(arr[i], end='')
            if i != len(arr) - 1:
                print(",", end='')
        print("]")
        
        
        

'''
뒤집는 행동을 직접 하지 않고 뒤집으면 반대쪽을 pop 하는 방식으로 진행
R 갯수 count 하는 것까지는 비슷했는데 마지막 저 reverse 하지 않고 왔다갔다 pop 하는 저걸 깨달아야 했음
'''