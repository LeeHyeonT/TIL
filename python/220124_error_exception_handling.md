[toc]

# 에러 / 예외 처리(Error / Exception Handling)



## 1. 디버깅

- branches

  모든 조건을 커버하는지??

- for

  반복문 원하는 횟수? 반복문 값이 결과값? 혹은 진입값??

- while

  종료조건 잘 되었는지?

- function, method

  input, return, parameter?

## 2. 에러들

### 1) Syntax Error (문법 에러)

파이썬 프로그램 자체가 실행되지 않음! 초보자가 가장 우선적으로 고쳐나가야 할 에러!



### 2) 예외(Exception)

- ZeroDivisionError : 0으로 값을 나눌 때
- NameError: 이름을 찾을 수 없을 때
- TypeError: 타입의 불일치 / argument 누락 / argument 갯수 초과 / argument type 불일치
- ValueError: 타입은 올바르나 값이 적절하지 않거나 없음
- IndexError: 인덱스 존재 x, 범위 벗어나는 경우
- KeyError: dictionary에서 해당 key 존재하지 않는 경우
- ModuleNotFoundError: 해당 모듈을 찾을 수 없는 경우
- ImportError: 모듈은 있으나 존재하지 않는 클래스/함수 사용할 경우
- KeyboardInterrupt: 임의로 프로그램 종료하는 경우
- IndentationError: 들여쓰기(Indentation) 가 적절하지 않은 경우



## 3. 예외 처리

try문 except 예외 (finally 명령문) 구조



## 4. 예외 발생시키기

raise <표현식>(메시지): 여러 에러에 따라 메시지 남기기 

assert<표현식>(메시지): 특정 상황에서 에러 발생시키고 메시지 남기기