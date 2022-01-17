[toc]

# 제어문

코드의 선택적 실행(조건), 반복적 실행(반복)을 위해 필요함

***tab(space 4칸) 잘 유지해야한다!!!***

## 1. 조건문

### if 활용 코드

```python
num = int(input('숫자를 입력해주세요 : ')) 
print(num)
if num % 2 == 1:			# if num % 2: 만 해도 가능
    print('홀수입니다.')
else:
    print('짝수입니다.')
```

- input을 int로 감싼 이유: **input은 작성한 값을 무조건 str값**으로 읽어 if문을 수행할 수 없음

  따라서 숫자값을 사용하기 위하여 int로 감싼 것!

- % 2 하면 나오는 값은 0 아니면 1: 0은 false, 1은 true

  list에서 [ ] 내부 비어있으면 false, 차 있으면 true

### elif 활용 코드

```python
dust = int(input('오늘의 미세먼지량 : ')) 

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

### 중첩 조건문 활용 코드

```
```

### 조건 표현식

```python
value = num if num >= 0 else -num
```

절댓값 나타내는 코드!

**"참일때 값 if 조건 else 거짓일 때 값"**

---

---

## 2. 반복문

### While문

**조건이 참**일 경우 반복적으로 코드 실행

**조건을 어떻게 짤 것인지 잘 생각해볼 것!!**

***종료조건이 반드시 필요!***

```python
# 사용자가 입력한 양의 정수 저장
user_input = int(input())
# 값 초기화, 결과를 나타낼 변수 지정
n = 0
total = 0
# while문
while n <= user_input:
    total += n
    n +=1
print(total)
```

**어떠한 값을 나타내고 초기화할 것인지 잘 캐치해 내는 것이 중요하다!!**

---

### For문

**"for 객체 in 시퀀스"** 의 형식으로 진행

**결과 담을 변수의 초기화 생각할 것!!**

#### 단순히 순회

```python
chars = input()
for char in chars:
    print(char)
```

#### index로 접근

```python
chars = input()
for idx in range(len(chars)):
    print(idx, chars[idx])
```

두 가지 방법 모두 잘 알고 있어야!!

#### Dictionary 순회

기본적으로 key를 순회, key를 이용하여 값을 활용함

```python
grades = {'kim': 80, 'lee': 100}

#1. dictionary 순회 --> key가 나옴!

for key in grades:
    print(key, grades[key])
    
#2. keys 이용 

for key in grades.keys():
    print(key, grades[key])
    
#3. value만

for value in grades.values():
	print(value)
    
#4. items 이용

for key, value in grades.item():
    # key, value = ()
    print(key, value)
    
print(grades.items())
```

#### enumerate 순회

(index, 'object') 로 묶인 tuple 로 list를 뽑아낼 수 있음

```python
chars = 'happy'

for idx, value in enumerate(chars):
    
```

#### List comprehension

```
```

#### Dictionary comprehension

```
```



### cf) 반복, 조건문 이용하여 코드작성

```python
# 1~30까지 숫자 중 홀수만 합하여 출력

# 빈 통 만들기
numbers = []

for i in range(1,31):
    if i % 2 == 1:
        numbers.append(i)
print(numbers)

# 한 줄 방법
numbers_2 = [i for i in range(1,31) if i % 2 == 1]
print(numbers_2)
```

### 반복문 제어

- Break

  반복문 종료

- Continue

  현재 반복 종료, 다음 반복 실행

- Pass

  있으나 마나, 코드 구조 잡을 때 임시로 쓰는 경우만 존재

- else

```python
is_b = False
for char in 'banana'
	if char == 'b':
        is_b = True
        break
        
if is_b:
    print('b가 있습니다')
else:
    print('b가 없습니다')
```



## 그 외

SyntexError : 문법 자체가 틀려서 나는 오류

pythontutor: 코드 실행 과정 볼 수 있는 사이트
