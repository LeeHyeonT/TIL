[toc]

# HTML, CSS

## 1. HTML

### 1) HTML 기본구조

- DOM(Document Object Model) 구조

  - html

    문서의 최상위 요소! (root 요소)

  - head

    문서 메타데이터 요소: 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

    일반적으로 브라우저에 나타나지 않음

    - title: 브라우저 상단 타이틀(주소)

    - meta: 문서 레벨 메타데이터

      링크 끌고왔을 때 정보 제공

    - link: 외부 리소스 연결 요소(CSS, favicon)

    - script: 자바스크립트 요소

    - style: CSS 직접 작성

  - body

    문서 본문 요소: 실제 화면 구성과 관련된 내용

    

- 요소(element)

  **<시작태그>내용<닫는태그> **의 형식이 기본적인 구조

  - 속성

    태그 별 사용 가능한 속성이 존재

    속성 내부에서 띄어쓰기 x, 쌍따옴표 사용할 것!

    태그와 상관 없이 사용 가능한 속성들도 존재

    - id: 문서 내 고유한 식별자 지정
    - class: 묶음들의 목록
    - data-*: 눈으로는 안 보이지만 어떠한 데이터를 사용할 때 사용
    - style: inline 스타일
    - title: 요소에 대한 추가 정보 지정
    - tabindex: 요소의 탭 순서

  

- 시멘틱 태그

  div로 다 구분하는 걸 ***의미를 담아서***  태그를 생성함, **그거 자체로는 기능은 없음**

  코드의 가독성 높이고 유지보수를 쉽게 할 수 있음

  cf) h1도 시멘틱 태그: 그 안이 제목이니 크기가 커져라 라는 기능이 담겨저 나온 것

  - header
  - nav
  - aside
  - section
  - article
  - footer

### 2) HTML 문서 구조화

인라인/블록

인라인: 내부 어울림

블록: 자리 차지

- \<a>\</a>: href 속성 활용, 다른 URL로 이동 가능하도록 함

- 그냥: \<b>\</b> / 시멘틱 표현: \<strong>\</strong>: 굵은 글씨 표현

- 그냥: \<i>\</i> / 시멘틱 표현: \<em>\</em>: 이탤릭체 

- \<br>: 줄 바꿈

- \<img>: src 속성 활용하여 이미지 표현 / alt 속성: 대체값(alternative): 대체 택스트 표현

- \<span>\</span>: 아무 의미 없는 인라인 컨테이너

- \<div>\</div>: 아무 의미 없는 블록 컨테이너

- \<p>\</p>: 하나의 문단 표현

- \<hr>: 수평선 표현(horizontal rule)

- \<ol>\</ol>: 순서 있는 리스트(1,2,3)

- \<ul>\</ul>: 순서 없는 리스트(점)

- \<pre>\</pre>: 작성한 내용 그대로 표현, 공백 유지

- \<blockuote>\</blockuote>: 텍스트가 긴 인용문 표현, 들여쓰기 한 것처럼 보임

- \<table>

- \<form>

  - get: 내용 그대로 전달
  - POST: 내용 숨겨서 전달

- \<input>

  - name: form control에 적용되는 이름

  - value: form control에 적용되는 값

  - type: input의 방식을 결정

  - input label

    label의 for, input의 id 가 서로 묶여서 사용됨

---

---

## 2. CSS

선택하고, 스타일을 지정한다(속성을 정해 값을 선택한다!)

웬만하면 외부 참조 형식으로 사용할 것! 수정할 것 있을 때 외부 참조 파일만 수정하면 되니 좋다!

### 1) CSS Selectors

- selectors

  - 전체 선택자: *

  - 요소 선택자: <> 안에 있는 녀석

  - 클래스 선택자: \<div class=""> 에서 "" 내부에 있는 녀석

    마침표(.) 으로 시작!

  - id 선택자: 해당하는 id값 녀석

    \# 문자로 시작!

  - **자식 결합자: 해당하는 클래스 바로 밑의(indentation 2칸 되어있는 녀석들) 요소 안에 있는 녀석**

    **" \> \> \> "** 이런 식으로 부등호로 표현!

  - **자손 결합자: 해당하는 클래스 안의 모든 요소 녀석들**

- 적용 우선순위

  !important 작성 > 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element > CSS 파일 로딩 순서

- pseudo-class (의사 클래스)

  어떤 녀석의 특정 기능을 할 때 작용하도록 하는 것

  ​	ex) :hover --> 마우스 위에 글씨를 올렸을 때 작용

- pesudo-element(의사 요소)

  어떠한 요소를 추가하면서 작용하도록 하는 것

  ​	ex) ::after --> 뒤에 특정한 글자 넣어줌

- attribute selector(요소 셀렉터)

  [ ] 안에 표현, 어떤 요소를 가지고 있는 녀석들에 대해 작용

- CSS 상속

  text관련 요소는 상속 가능, box model관련 요소는 상속 불가, 찾아가면서 하자...

---

### 2) CSS 단위

#### 크기 단위

- px

- %

- em

  배수 단위 / 바로 위 부모 요소에 대한 상속 영향을 받음

- rem

  배수 단위 / 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐

- viewport

  디바이스 viewport를 기준으로 상대적인 사이즈 결정

  모바일, 웹 모두 사용할 시 이거 써야할 듯!

  vw, vh, vmin, vmax

#### 색상 단위

색상 키워드

rgb 색상

HSL 색상

투명도 표현할 때는 a 뒤에 붙여서!

#### CSS 문서 표현

찾아서 쓰자....

----

### 3) Selectors 심화

#### 자손 결합자

selector 하위의 모든 selector 요소

띄어쓰기로 표현

#### 자식 결합자

selector 바로 아래의 selector 요소

\> 로 표현

#### 일반 형제 결합자

selector 형제 요소(indentation 같은 녀석들) 중 뒤에 위치하는 selector 모두 선택

~ (물결) 로 표현

#### 인접 형제 결합자

selector 형제 요소 중 바로 뒤에 위치하는 selector 요소 선택

\+ 로 표현



### 4) Box model

***모든 요소는 네모, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다!*** 이런 형식을 normal flow

#### content

글, 이미지 등 요소의 실제 내용

#### padding

테두리 안쪽의 내부 여백 

배경색 적용, 이미지는 padding까지 적용

#### border

테두리

#### margin

무조건 빈 값, 배경색 x

shorthand로 표현 시 시계 방향으로 표현, 정의 안 된 곳은 반대편 것 가져온다

### 5) Display

#### block

줄바꿈이 일어남, 화면 크기 전체 가로 폭 차지, block 안에 inline 요소 들어갈 수 있음

div, ul, ol, li, p, hr, form 등

#### inline

줄바꿈 x, content 너비만큼 가로 폭 차지,  width, height, margin-top, margin-bottom 지정 불가

상하 여백은 line-height 로 지정

span, a, img, input, label, b, em, i, strong 등

#### inline-block

block과 inline 레벨 요소와 특징 모두 가짐

#### none

해당 요소를 화면에서 제거, 공간도 제거

cf) visibility: hidden --> 해당 요소를 화면에서 제거, 공간은 유지



### 6) Position

#### relative

static 위치 기준으로 이동! 이동해도 그 static 위치는 차지하고 있음

#### absolute

기존 위치에서 완전히 벗어나 이동! 위치 차지 또한 사라짐

relative한 녀석 기준 있어야 원하는 대로 이동할 것, 기준잡을 곳 없다면 body 기준으로 이동함

#### fixed

화면 어딘가에 고정되어 나타남

---

---

## 3. 개발자 도구





## 기타 팁

모르는 것 있으면 **"mdn 모르는 것"** 이런 형식으로 검색하면 좋다!

vscode에서 문서 작성 후 **alt+b** 누르면 웹페이지상에서 확인 가능

vscode에서 lorem 치면 랜덤 문자 나온다! 

vscode에서 ! 치고 엔터/탭 누르면 기본 세팅 나온다! 기본 세팅 내 body에서 작성할 예정

https://www.w3.org/TR/CSS21/propidx

상속 관련 확인!