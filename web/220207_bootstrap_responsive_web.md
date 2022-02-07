[toc]

# Bootstrap

기존의 기본 html 내 css, js설정을 좀 더 예쁘게? 깔끔하게? 만들어주는 오픈소스 파일

## CDN

여러 컨텐츠들(css, js image 등) 을 효율적으로 전달하기 위해서 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

복사-붙여넣기로 파일에 넣어 사용, css파일 link 걸지 않고 bootstrap css 파일 사용 가능

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
```



## spacing

### 1) 글씨

- m-1: 0.25rem --> 4px
- m-2: 0.5rem --> 8px
- m-3: 1rem
- m-4: 1.5rem
- m-5: 3rem

### 2) 공간

- mx- : margin-right, margin-left값
- my- : margin-top, margin-bottom 값
- px- : padding 마찬가지
- py- : padding 마찬가지



## color

class 자리에 들어감, 다양하고 예쁜 색상 존재!

text에 색 넣으면 text-primary 이런 식이고 배경화면에 색 넣으면 bg-secondary 이런 식!

---

---

# Bootstarp grid system

## grid system

Column: 실제 컨텐츠를 포함하는 부분 

Gutter: column-column 사이 공간(이격)

Container: column들을 담고 있는 공간

위 개념 이용, flexbox로 제작하여 container, row, col 으로 컨텐츠 배치하고 정렬

column은 총 12개!

## breakpoints

xs < sm < md < lg < xl < xxl 크기 순

.col- < .col-sm- < .col-md- < .col-lg- < .col-xl- < .col-xxl-

## nesting

한 row 안에 또 다른 row 넣어서 한 공간을 쪼개어 표현

## offset

앞에서부터 뛰어 넘어서 배치하는 것

다른 것과 똑같이 12column 안에서 작용!

 

# Responsive web

bootstrap 을 이용하여 responsive web을 만들 수 있다!!



## 기타

https://getbootstrap.com/docs/5.1/getting-started

여기서 여러 구조들, 이름 짓는 것들 많이 보고 익힐것!
