import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 최대 500,500번 반복하는 문제?
string = input()
len_count = 1
answer_count = 0
while True:
    if len_count > len(string) - 1:
        break
    answer_set = set()
    for i in range(len(string) - len_count + 1):
        word = string[i:i+len_count]
        answer_set.add(word)
    answer_count += len(answer_set)
    len_count += 1

print(answer_count+ 1)

'''
통과는 했지만 아쉬운 문제
slicing 을 사용하지 않는다면 효율적으로 문제를 풀어낼 수가 없었다...
답을 안 보고 slicing 을 떠올린 것은 고무적
+ 다른 사람들의 답을 살펴보다가 다음의 코드를 발견
a = input()

if len(a) == 1:
  cnt = 0
else:
  cnt = 1
  for i in range(1, len(a)):
    li = []
    for j in range(0, len(a) - i + 1):
      li.append(a[j: j + i])
    cnt = cnt + len(set(li))

print(cnt)

걸린 시간은 비슷했으나 메모리 사용량이 거의 1/8 수준
아마 list 내부를 계속 reset 시켜줘서 그런듯!
+ 확인 결과 맞다!
+ 내 코드도 그렇게 바꿔놓음
'''