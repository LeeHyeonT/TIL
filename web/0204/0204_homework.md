# 0204_homework

## 1. Semantic Tag

header, section, footer



## 2. input Tag

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="#">
    <span class="username" onclick="document.getElementsByName('username').focus()">USERNAME : </span>
    <input type="text" name="username" id="username" placeholder="아이디를 입력 해 주세요"><br>
    <span class="pwd" onclick="document.getElementsByName('pwd').focus()">PWD : </span>
    <input type="text" name="pwd" id="pwd" placeholder="**********">
    <input type="submit" value="로그인">
  </form>
</body>
</html>
```



## 3. 크기 단위

rem



## 4. 선택자

자손 결합자: \<div> \</div> 사이에 존재하는 모든 \<p> \</p> 안의 요소에 대하여 글씨 색을 crimson으로 합니다.

자식 결합자: \<div> \</div> 사이에 존재하는 \<p> \</p> 가 많을 경우 첫 번째 \<p> \</p> 안의 요소에 대해서만 글씨 색을 crimson으로 합니다.