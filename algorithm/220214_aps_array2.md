[toc]

# APS(Algorithm Problem Solving)

# --> Array 2



## 배열: 2차원 배열

1차원 list를 묶어놓은 list

[[0,1,2],[1,2,3]] 이런 식으로!

```python
N = int(input())
# 붙어있는 문자열
arr = [list(map(int, input())) for _ in range(N)]
# 떨어져있는 문자열
arr = [list(map(int, input().split())) for _ in range(N)]
```



2중 for문으로 배열 순회를 진행한다

- *** 주로 행: i , 열, j 로 표현한다 ***

- 지그재그 순회

  j  /  (m-1) -j 를 왔다갔다해야하기에 j + (m-1-j-j) * (j%2) 이런 식으로 표현한다

인접 배열 요소 찾는 법

```python
# 동쪽부터 시계방향으로 보게 해주는 방향자
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# N*N 행렬 arr 존재
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 유효한 index 한 번에 표현
            if 0 <= ni < N and 0 <= nj < N:
                print(i,j,arr[ni][nj])
```

---



## 부분집합 생성

\***완전검색**\*기법으로 부분집합 만들기!

```python
'''for문 활용하여 만들기: 갑자기 바뀌는 부분이 생기면 사용 불가

bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit.....
'''
```

- 비트 연산자

  - \& : 비트 단위로 AND 연산을 한다

  - | : 비트 단위로 OR 연선을 한다

  - \<< : 피연산자의 비트 열을 왼쪽으로 이동시킨다

    - 1<<n: 해석해보면 원소가 n개일 경우의 모든 부분집합의 수를 의미!

  - \>> : 피연산자의 비트 열을 오른쪽으로 이동시킨다

  - 종합

    i & (1<<j): i의 j번째 비트가 1인지 아닌지 검사! 하는 뜻으로 해석할 수 있다.

  이 비트 연산자를 이용해서 부분집합을 보다 간결하게 표현 가능하다!

```python
arr = [3, 6 ,7, 1, 5, 4]
# n: 원소의 갯수
n = len(arr)

for i in range(1<<n):				# 1<<n : 부분집합의 갯수 
    for j in range(n):				# 원소의 수만큼 비트를 계산 (2^6 이므로 6개 계산)
        if i & (1<<j):				# i의 j번 비트가 1인 경우 
            print(arr[j], end=", ")
    print()
print()
```

---



## 바이너리 서치 (Binary Search)

저장되어 있는 자료 중에서 원하는 항목을 찾는 작업 중 하나!

\***자료의 가운데**\* 에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

**자료가 정렬된 상태** 여야 할 수 있다!!

```python
def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return true					# 검색 성공
        elif a[middle] < key:
            end = middle - 1
        else:
            start = middle + 1
    return false						# 검색 실패
```



## 셀렉션 알고리즘 (Selection Algorithm)

저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법!

---



## 선택 정렬 (Selection Sort)

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

\****Bubble Sort 와의 차이점을 설명할 줄 알아야 한다!!!!\****

```python
def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j						# 자리바꿀 녀석 설정
        a[i], a[minIdx] = a[minIdx], a[i]		# 자리바꿈
```



---

---

# 기타

pycharm 디버거 사용할 때

print(locals()): 사용 중인 지역 변수들 출력

print(globals()): 사용 중인 글로벌 변수들 출력