[toc]

# 데이터 구조 (Data Structure) 메소드(method)



## 순서가 있는 데이터 구조



### 1. 문자열(String)

**immutable!!** 

#### 1) 많이 쓰는 것들

- find(x)

x의 첫 번째 위치를 반환(index값), ***없으면 -1을 반환***

- index(x)

x의 첫 번째 위치를 반환(index값), ***없으면 오류 발생***

- .isalpha()

알파벳 여부 T/F

- .isupper()

대문자 여부 T/F

- .islower()

소문자 여부 T/F

- .istitle()

타이틀 형식 여부 T/F

공백 기준 앞,뒤 첫 문자 + 어퍼스트로피 에스 가 대문자인지의 여부 



#### 2) 다른 것들

- .replace(old, new[count])

  old값을 new로 바꿈, 다 안바꾸고 싶으면 count 작성

- .strip([chars])

  특정 문자열 지정, 왼쪽(.lstrip) 혹은 오른쪽(.rstrip) 제거

  문자열 지정하지 않을 시 공백 제거

- .split('sep')

  문자열을 sep 에 따라서 쪼개어 list로 반환

- 'sep'.join([iterable])

  iterable한 컨테이너 요소들을 sep 으로 합쳐 문자열으로 반환

  ***[iterable] 에 str 타입이 아니면 TypeError 발생!!***



### 2. 리스트(List)

#### 1) 쓰는 것

- .append(x)

  리스트에 값을 추가함

-  .extend(iterable)

  리스트에 iterable의 항목을 추가함

  문자 하나하나 추가하지 않게 조심할 것!

- .insert(i,x)

  정해진 위치 i 에 x 값 추가함

- .remove(x)

  리스트에서 값이 x인 것 삭제

  모양 자체를 넣어야 함

- .pop(i)

  정해진 위치 i 에 있는 값을 삭제, 그 항목 반환

  i  가 지정되지 않는다면 마지막 값을 삭제하고 그 항목 반환

  index 번호를 넣어야 함

- .clear()

  모든 list값 삭제하고 빈 list 가 됨

- .index(x)

  x값의 index 반환함

- .count(x)

  원하는 값의 갯수를 반환함

- .sort()

  list를 정렬시킴. 원본이 바뀌는 것

  (cf) sorted([list]): 함수: 원본이 바뀌는 건 아니고 함수 사용할 때 잠깐 정렬되는 것)

- .reverse()

  list 순서를 반대로 바꿈



### 3. 튜플(Tuple)

- 변경 불가하기때문에 값에 영향을 미치지 않는 메소드만 존재
- 리스트 메소드 중 항목 변경하는 메소드 제외하고 나머지는 동일함

---

---

## 순서가 없는 데이터 구조



### 1. 셋(Set)

#### 1) 많이 쓰는 것

- .add(elem)

  셋에 elem 값을 추가

- .update(*others)

  셋에 여러 값을 추가

- .remove(elem)

  셋에 elem 값을 삭제, ***없다면 KeyError***

- .discard(elem)

  셋에 elem 값을 삭제, ***없어도 에러 발생하지 않음***

- .pop()

  셋에 들어있는 **임의의** 원소를 제거하고 반환함



### 2. 딕셔너리(Dictionary)

#### 1) 쓰는 것

- .get(key[default])

  key를 통해 value를 가져옴

  KeyError 발생하지 않고 default 값 설정 가능

- .pop(key [, default])

  key가 딕셔너리에 있으면 제거하고 남은 값들을 반환함

  그렇지 않으면 default 반환

  default 값 없으면 KeyError

- .update

  제공된 key, value로 덮어씀

---

---

## 얕은 복사와 깊은 복사(Shallow, Deep Copy)

### 1. 할당(assignment)

- 대입 연산자(=)

  일반적으로 두 값을 = 처리하여 놓으면 두 값은 하나의 객체를 바라보며 값을 끌어오는 것이기에

  어느 한 값의 데이터를 바꾸면 다른 한 값도 같이 바뀌게 된다.

  이럴 때는  = 처리 할 값에 대해 바로 그 변수를 넣지 말고 어떤 형태로 덮어씌워서 = 에 대응시킨다.

### 2. 깊은 복사

- import copy 하고 copy.deepcopy 사용
- 리스트 내의 리스트 내의 값 변경에 대해서 값 변동이 이루어지지 않게 됨

