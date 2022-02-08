# 0208_homework

## 1. CSS flex-direction

flex-row: main-axis 를 가로로 하여 진행합니다.

flex-row-reverse: main-axis를 가로로 하고 그 방향을 오른쪽에서 왼쪽으로 하여 진행합니다.

flex-column: main-axis를 세로로 하여 진행합니다.

flex-column-reverse: main-axis를 세로로 하고 그 방향을 아래쪽에서 위쪽으로 하여 진행합니다.



## 2. Bootstrap flex-direction

```html
<div class="d-flex flex-row"></div>
<div class="d-flex flex-row-reverse"></div>
<div class="d-flex flex-column"></div>
<div class="d-flex flex-column-reverse"></div>
```



## 3. align-items

align-items-start: cross-axis의 맨 위에 요소들을 배열합니다.

align-items-end: cross-axis의 맨 끝에 요소들을 배열합니다.

align-items-center: cross-axis의 중앙에 요소들을 배열합니다.

align-items-baseline: cross-axis의 기준선에 요소들을 배열합니다.

(align-items-stretch: 높이를 cross-axis의 길이와 같게 하여 요소들을 배열합니다. 기본값입니다.)

## 4. flex-flow

(1) flex-direction, flex-wrap 의 축약형입니다.



## 5. Bootstrap Grid System

(a) container

(b) row



## 6. Breakpoint prefix

1\) breakpoint의 약자가 들어갑니다. breakpoint는 반응형 웹 구조에서 너비의 기준을 잡아 일정 너비 이상이 될 시 요소의 크기의 변화를 만들어낼 수 있습니다. 아무것도 안 들어갈 수도 있고 크기가 작은 순서대로 sm, md, lg, xl, xxl 이 들어갈 수 있습니다.

2\) 0~12 사이의 정수가 들어갑니다. flexbox에서는 한 container를 12개의 column으로 구분하여 크기를 배분하는데  그 숫자가 클수록 크기가 커집니다. 0~12 사이의 정수가 모두 들어갈 수 있지만 정렬을 쉽게 하기 위해서 보통 12의 약수를 넣습니다.