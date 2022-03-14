[toc]

# 1. Database

데이터베이스(DB): 조직적인 데이터들의 모임



## RDB(관계형 데이터베이스)

Relational Database

key, value 값들의 간단한 relation으로 표현된 데이터베이스

### 용어 정리

- schema(스키마): 데이터베이스에서 자료 구조, 표현방법 , 관계 등 전반적인 관계 명세에 관한 것
- table(테이블): 열(컬럼/필드), 행(레코드/값)의 모델을 사용하여 조직된 데이터 요소들의 집합

- column(열): 각 열에 고유한 데이터 형식이 지정됨
- row(행): 실제 데이터가 저장되는 형태
- Primary Key(고유 키): 각 행의 고유값 / 반드시 설정!!



## RDBMS(관계형 데이터베이스 관리 시스템)

Relational Database Management System

SQLite 를 기반으로 배워볼 예정!

---

----

# 2. SQLite

비교적 가벼운 데이터베이스!

## SQLite Data Type

- Null
- INTEGER: 8바이트에 저장된 부호 있는 정수
- REAL: 8바이트 부동 소숫점 숫자로 저장된 부동 소숫점 값 (실수)
- TEXT
- BLOB: 입력된 그대로 저장되는 것(텍스트가 아닌 모든 것)

### SQLite Data Affinity

1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC

순서로 선호도를 갖는다! 위에서 나온 5가지 타입만 사용한다고 보면 된다!

## 실행 방법

vscode terminal에서

`sqlite3 이름.sqlite3`

하고 

`.database`

까지 하고 진행하면 백지에서 시작!

만약 원래 존재하는 파일 불러오고싶다면

(아래 예시에서는 csv 파일 읽어오는 것)

`.mode csv` --> csv 파일 읽는 모드

`.import 열고싶은csv파일이름.csv 만들고싶은테이블이름` 한 후

`.tables` 로 생성되었는지 확인

---

----

# 3. SQL

Structured Query Language

데이터 관리를 위해 특수 설계된 언어

DDL(데이터 정의 언어): 테이블, 스키마 정의

DML(데이터 조작 언어): CRUD

DCL(데이터 제어 언어)



## 1) DDL

**CREATE TABLE 테이블명 (요소값1 datatype (NOT NULL), 요소값2 datatype (NOT NULL), .....);**

: 테이블명 , 요소들 가진 테이블 생성

**DROP TABLE 테이블명;** : 테이블명 가진 테이블 삭제



**ALTER TABLE 기존테이블이름 RENAME TO 새로운테이블이름**; : 테이블 이름 새로운 이름으로 수정

**ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터type설정;** : 테이블에 새로운 컬럼 추가

여기서 NOT NULL 바로 추가할 수 없음

해결책: 1) NOT NULL 설정 없이 추가

​			  2) 기본값(default) 추가

​			  **ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터type NOT NULL DEFAULT '기본값';**



**RENAME COLUMN 기존컬럼이름 TO 새로운컬럼이름;** : 컬럼 이름 새로운 이름으로 수정

(3.35에 추가)

**ALTER TABLE 테이블명 DROP COLUMN 컬럼명;** : 테이블에서 컬럼명 가진 컬럼 삭제

## 2) DML

INSERT: C

SELECT: R

UPDATE: U

DELETE: D

위의 것들 실습!

- Create

  **INSERT INTO 테이블이름 (컬럼1, 컬럼2, ....) VALUES (값1, 값2, ....);**

  **INSERT INTO 테이블이름 VALUES (값1, 값2, ...전체 갯수 맞는 값 갯수);**

- Read

  - LIMIT: 특정 범위의 데이터만 가져옴 / OFFSET 과 같이 쓰이는 편
  - WHERE: IF문처럼 작용!
  - DISTINCT: 조회 경과에서 중복 행을 제거

  **SELECT 컬럼1, 컬럼2, .... FROM 테이블이름;**

  **SELECT 컬럼1, 컬럼 2, .... FROM 테이블이름 LIMIT 숫자;**

  **SELECT 컬럼1, 컬럼2, .... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;**

  **SELECT 컬럼1, 컬럼2, .... FROM 테이블이름 WHERE 조건;**

  **SELECT DISTINCT 컬럼 FROM 테이블이름;**

- Delete: 기본적으로 id값 재활용함! / AUTOINCREMENT 사용하여 재사용하는 것 방지: django 에서 이런 방식

  **DELETE FROM 테이블이름 WHERE 조건;**

- Update

  - SET

  **UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, .... WHERE 조건;**



### Where 활용

부등호, AND, OR 활용 가능



### Aggregate Functions

집계 함수!

값 집합에 대한 계산을 수행, 단일 값을 반환

- COUNT

  **SELECT COUNT(컬럼) FROM 테이블이름;**

- AVG

  **SELECT AVG(컬럼) FROM 테이블이름;**

- MAX

  **SELECT MAX(컬럼) FROM 테이블이름;**

- MIN

  **SELECT MIN(컬럼) FROM 테이블이름;**

- SUM

  **SELECT SUM(컬럼) FROM 테이블이름;**



### LIKE

패턴 맞추는 것!

2개의 wildcards 제공

- %

  0개 이상의 문자: 이 자리에 문자열이 있을 수도, 없을 수도 있다.

- _

  임의의 단일 문자: 반드시 이 자리에 한 개의 문자가 존재해야 한다.

**SELECT * FROM 테이블이름 WHERE 컬럼 LIKE 'wildcard 패턴';**



### ORDER BY

조회 결과 집합을 정렬!

2개의 keywords 제공

- ASC: 오름차순(default)
- DESC: 내림차순

**SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC**

**SELECT * FROM 테이블이름 ORDER BY 컬럼1, 컬럼2, .... DESC;**

정렬할 때 ***컬럼 순서*** 가 중요하다! 먼저 나온 컬럼대로 정렬하고 그 다음 컬럼은 먼저 나온 컬럼대로 정렬한 값 가지고 다시 정렬하는 것! 컬럼1, 컬럼 2 순!



### GROUP BY

행 집합에서 요약 행 집합을 만듦?

데이터 모음에서 다시 요약하여 집합을 만듦!

\** WHERE 절이 포함된 경우 WHERE 절 뒤에 작성해야 한다!!! **

**SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블이름 GROUP BY 컬럼1, 컬럼2, ....;**

**SELECT 컬럼1, aggregate_function(컬럼2) AS 해주고픈이름 FROM 테이블이름 GROUP BY 컬럼1, 컬럼2, ....;** 