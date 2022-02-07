[toc]

# CSS Layout

## 1. float

박스를 왼쪽 혹은 오른쪽으로 이동, 텍스트 포함 **인라인 요소** 들을 wrapping

Normal flow를 벗어남!

clearfix를 습관적으로 해 주자! (이름은 꼭 clearfix가 아니여도 되지만 대부분 이렇게 이름짓는 편)

```css
.clearfix::after{
content=""
display=block
clear=both
}
```



## 2. Flexbox (중요!!!!)

행, 열 형태로 아이템들을 배치하는 **1차원 레이아웃 모델**

축: main axis(메인), cross axis(교차)

main axis를 기준으로 함

구성 요소: Flex Container(부모), Flex Item(자식)

### 배치 설정

#### - flex-direction

main axis 기준 방향을 성정

역방향이라면 html 태그 선언 순서와 시각적으로 반대이니 유의!

- row
- row-reverse
- column
- column-reverse

#### - flex-wrap

컨테이너 영역을 벗어나지 않도록 하여 배치

- wrap

  넘치면 그 다음 줄에 배치

- nowrap

  기본값, 한 줄에 배치

#### - justify-content

main-axis를 기준으로 공간을 배분

- flex-start

  좌측 정렬

- flex-end

  우측 정렬

- center

  가운데 정렬

- space-between

  가운데 item 기준으로 사이 간격 동일

- space-around

  item들 margin 값 동일

- space-evenly

  border-item, item-item 간 간격 동일

#### - align-content

cross axis를 기준으로 공간 배분

아이템이 한 줄로 배치되는 경우 확인 불가!

justify-content와 가짓수 같음

#### - align-items

모든 item을 cross axis를 기준으로 정렬

- stretch
- flex-start
- flex-end
- center
- baseline

##### align-self

*** 얘만 개별 item***을 cross axis 기준으로 정렬!

- stretch
- flex-start
- flex-end
- center

#### - 기타: class 이름 적는 곳에 들어감

flex-grow: 남은 영역 그 아이템에 분배, 전체 비율이 아닌 남은 공간에 대한 비율! 

order: 배치 순서 부여
