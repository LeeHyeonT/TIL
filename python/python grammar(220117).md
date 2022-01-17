[toc]

# python 문법

스타일 가이드 PEP8 이용 예정

## 1. 가이드

', ' " " 은 하나만 골라서 작성하기

= 은 앞 뒤 띄어쓰기 하기

들여쓰기는 space 4번(4칸)으로 통일

**주석: ctrl/** 하면 한 번에 가능!

**''' 글자 '''** 하면 다른 줄까지 한 번에 주석 가능

## 2. 변수(Variable)

상자 안에 어떤 것을 넣어서 보관하고 있는 것

'이름 = 값' : 여기서 **= 은 할당하다** 라는 뜻으로 사용

**변수의 type() 을 확실하게 알아야 한다!!**



### 변수 연산

- 임시 변수 : 임시로 상자 하나를 가지고 와서 그 곳에 잠깐 보관하는 느낌

- 식별자(Identifiers) 

  첫 글자에 숫자 x, 영문알파벳, _ , 숫자로 구성

  - Camel Case : RedApple 같이

  - Snake Case : red_apple 같이

    **Snake Case를 더 많이 씀**
    
    

### 자료형

크게 Boolean, Numeric, String 세 가지 type

None type 존재 : **값이 존재하지 않다** 라는 것을 의미하기 위해 사용

#### 1) Boolean

true/false 로 값 변환

빈 값, 0값, [], (), {}은 false로 반환

bool 사용

#### 2) Numeric

- 정수는 모두 int

  매우 큰 수의 산수 overflow 발생하지 않음!

  2진수: 0b, 8진수: 0o, 16진수: 0x 말머리 붙이고 작성 (binary, octal, hexa)

- 정수가 아닌 실수는 모두 float

  rounding error: 컴퓨터 연산에서 어쩔 수 없는 과정

  ex) 3.14 - 3.02 = 0.1200000000001 이라서 3.14 - 3.02 == 0.12 하면 F 나온다

  math 함수를 사용하여 모자라는 디테일 채워줌

  --> math.isclose(a,b) 하면 True 나옴, 이거 이용

- 복소수는 complex, 그냥 알아만 놓자

#### 3) String

모든 문자는 str

위에서도 말했지만 '', "" 중 하나만 선택 후 사용

immutable 성질: 중간 한 글자만 바꾸는건 불가능, 바꾸려면 전체적으로 다시 정의내려야

Iterable 성질: 하나하나 떼어서 접근, 활용 가능

- Escape sequence

  \n : 줄 바꿈(new line)

  \t : 탭(tap)

  따옴표 표시: md파일에서의 \ 와 같은 방법

- 문자열 변수로 만들기

  %-formatting : %알파벳 하여 변수 type 설정

  str.format() : 뒷부분에 format 작성

  f-strings : 가독성 위해 str 넣으면서 format 넣어 작성
  
  **str.format() 이랑 f-strings 은 잘 알고 있어야!**

---

---

## 3. 컨테이너(Container)

여러 개의 데이터를 담아놓은 객체(object)

시퀀스 : 순서 있음, 비시퀀스 : 순서 없음

**index 는 숫자 0부터 시작!! 거꾸로 갈거면 -1부터 작아지는 순서로**

### 시퀀스형

#### 1) List

가변 자료형

항상 대광호 형태로 출력: [  ]

대괄호가 많으면 왼쪽 대괄호부터 하나씩 꺼내서 정리

#### 2) Tuple

불변 자료형

항상 소괄호 형태로 출력:  (  )

단일 항목 생성 시 값 뒤에 , 붙여야 함

일반적으로 파이썬 내부에서만 어떤 것을 묶기 위해 활용

#### 3) Range

숫자의 시퀀스 나타냄

range(n) : 0부터 n-1까지

range(n,m) : n부터 m-1까지

range(n,m,s) : n부터 m-1까지 s씩 건너뛰면서



### 비시퀀스형 : 순서 x

#### 1) Set

가변 자료형

중복없이 **순서가 없는** 자료구조

set() 이나 중괄호 이용: {  }

#### 2) Dictionary

키-값(key-value) 쌍으로 이루어진 객체 잠조

key: 불변 자료형(immutable)

value: 자유로운 형태

dict() 나 중관호 이용: {  }



### Type들 간 변환(Typecasting)

Implicit(파이썬 내부에서), explicit(내가 의도적으로) 두 가지 형태

어느 형태라도 range, dictionary 형태로 변환은 불가능

dictionary를 다른 형태로 변환시키면 key만 나옴

- Implicit

  True를 1로, int형을 float형으로, 실수를 복소수로....

- explicit

  int, float, str로....

  ![컨테이너 간 변환](%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%20%EA%B0%84%20%EB%B3%80%ED%99%98.PNG)

---

---

## 4. 연산자(Operator)

### 산술 연산자

/ : 나눗셈, 결과는 항상 float

// : 몫

%(modulo) : 나머지 --> 홀짝 구분할 때 많이 쓰임

### 비교 연산자

== : 같음

!= : 같지 않음

True/False 값 반환

### 논리 연산자

A and B : A,B 둘 다 True어야 True, 아니면 False

A or B : A,B 둘 다 False 어야 False, 아니면 True

True/False 값 반환

### 복합 연산자

+= : 변수에 1 더함

### 식별 연산자

is : none 파악할 때 씀

### 멥버십 연산자

in, not in : 안에 포함되어있는지 확인

### 시퀀스형 연산자

시퀀스들끼리 합쳐줌

[1,2] + [3] 하면 [1,2,3]

시퀀스 반복

[1,2] * 3 하면 [1,2,1,2,1,2]

### 인덱싱(Indexing)

시퀀스 내의 특정 인덱스 값에 접근!

### 슬라이싱(Slicing)

시퀀스를 쪼개서 표현

### set 연산자

| : 합집합

& : 교집합

\- : 여집합

^ : 차집합

---

