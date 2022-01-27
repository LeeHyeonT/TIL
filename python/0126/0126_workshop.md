# 0126_workshop

## 1. pip

(1) PyPI에 인덱싱된 python package 중 faker 라는 repository 내에 있는 파일들을 묶은 패키지를 설치한다.

(2) 명령 프롬프트에서 실행해야 한다.

## 2. Basic Usages(https://github.com/joke2k/faker#basic-usage)

1. faker라는 모듈에서 Faker라는 클래스의 사용을 하기 위한 코드이다.
2. Faker는 클래스, fake은 인스턴스 이다.
3. name()은 fake의 인스턴스 메서드 이다.

## 3. Localization(https://github.com/joke2k/faker#localization)

(a) init

(b) self

(c) Locale  = 'en_US'

## 4. Seeding the Generator(https://github.com/joke2k/faker#seeding-the-generator)

#1 : 'Margaret Boehm'

#2 : 'Margaret Boehm'

seed() 는 클래스 메서드이다.

## 4. Seeding the Generator

#1 : 'Margaret Boehm'

#2 :  '박진우' 같은 랜덤한 한국 이름이 나온다.

seed_instance() 는 인스턴스 메서드이다.

seed() 는 클래스 자체를 건드려  그 클래스의 인스턴스들이 모두 seed() 의 결과에 의해 나온 값을 이용할 수 있다.

seed_instance() 는 인스턴스만을 건드려 저 메서드를 사용하는 인스턴스에만 영향이 간다.