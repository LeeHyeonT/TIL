import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

from pprint import pprint
def solving(lst):
    # 문제에서 나온 암호 dictionary 로 저장
    password = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0110111": 8,
        "0001011": 9
    }
    # 10진수 저장할 리스트 생성
    str_10 = []
    for string in lst:
        str_10.append(password[string])
    # 문제의 조건에 맞게 처리할 새로운 리스트 생성
    tmp = []
    # 홀수 번째는 다 더하고 3 곱함
    for odd in range(0,len(str_10), 2):
        tmp.append(str_10[odd])
    tmp = tmp * 3
    # 짝수 번째는 그냥 다 더함
    for even in range(1, len(str_10), 2):
        tmp.append(str_10[even])
    # 처리한 값이 10의 배수라면 10진수 값들의 합, 아니라면 0 출력
    if sum(tmp) % 10 == 0:
        return print(f"#{tc} {sum(str_10)}")
    else:
        return print(f"#{tc} {0}")

def findpoint(lst):
    # 함수 바깥에서 끝 지점과 계산할 row 번호 쓸 것이기 때문에 전역변수로 지정
    global end_point
    global start_row
    # row 살펴봄
    for i in range(N):
        # 암호들을 보면 끝자리가 다 1로 끝나기에 배열에서 1로 끝나는 시점이 언제인지 찾을 것
        for k in range(M-1, M-56, -1):
            if lst[i][k] == str(1):
                end_point = k
                start_row = i
                return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 입력된 배열을 그냥 한 줄씩 str 값으로 받아옴
    arr = [input() for _ in range(N)]
    # 7자리씩 잘라서 저장해둘 리스트 생성
    storage = []
    # 배열에서 어디부터 어디까지가 암호인지 모르기에 그 시작점 및 끝점을 찾기 위해 함수 실행
    findpoint(arr)
    
    # 위에서 찾은 값 이용하여 storage 에 값 7개씩 잘라서 더해줌
    for j in range(end_point - 56 + 1, end_point-1, 7):
        storage.append(arr[start_row][j:j+7])
    
    # 10진수 변환 및 정답 도출 함수
    solving(storage)
