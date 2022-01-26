height = []

# input 9번 받기, int값으로 변환하여 list에 저장 
for _ in range(9):
    height.append(input())
    height_int = list(map(int,height))

# 숫자 9개니 9번 반복
for idx in range(9):
    # 반복할 때마다 list 초기값으로 되돌려야하므로 변수 설정해서 숫자 리스트 재생성
    height_remove_process = height_int[:]

   # 숫자 7개의 합이 100이 안 되는 경우는 없으므로 일단 숫자 하나를 제거하고 봄
    height_remove_process.remove(height_remove_process[idx])
    # 숫자 하나를 제거했으니 숫자 8개, 8번 반복
    for idx in range(8):
        # 남은 숫자들에서 각 index에 맞는 숫자 제거했을 때 나머지의 합이 100이면 그 index에 맞는 숫자 제거 후 break
        if sum(height_remove_process) - height_remove_process[idx] == 100:
            height_remove_process.remove(height_remove_process[idx])
            break
        else:
            continue
    # 여기로 왔다는 건 숫자 7개의 합이 100이라는 것이므로 break을 받기 위한 if문 작성
    if sum(height_remove_process) == 100:
            break
# 숫자 7개를 오름차순으로 정렬   
height_remove_process.sort()
# 숫자 7개를 차례로 프린트
print(*height_remove_process, sep = "\n")
