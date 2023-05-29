import sys
sys.stdin = open('input.txt', encoding='UTF-8')

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

ans = 0
for i in range(n):
    ans += a[i] * b[i]

print(ans)

'''
문제에서 b의 배열은 바꾸지 말라고했지만 어차피 우리가 구하는 것은 답 뿐이기에 b 배열도 정렬해도 무관하다.
하지만 정렬 후 a의 배열을 나타내라고 문제가 주어진다면 이 방법은 사용하지 못한다.
그 때는 두 배열을 복사하여 복사한 배열을 이렇게 정렬시킨 후 정렬된 배열의 각 숫자에 대응하는 index 값을 찾아 원래 배열의 해당 index를 바꿔주면 된다. 
'''