# 0203_workshop

## 1. img tag

```html
<img src="c:\Users\Windows_10\Desktop\TIL\ssafy/image/my_photo.png" alt="ssafy">
```



## 2. 파일 경로

(a) : 절대 경로

(b) : 상대 경로

```html
<img src="../img/my_photo.png" alt="ssafy">
```



## 3. Hyper Link

```html
<a href="https://ssafy.com">
  <img src="ssafy/image/my_photo.png" alt="ssafy">
</a>
```



## 4. 선택자

(1)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    #ssafy > p:nth-child(2){
      color: red;
    }
  </style>
</head>
<body>
  <div id="ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
</body>
</html>
```

첫번째 단락 의 글씨만 빨간색으로 변한다. 

(2)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    #ssafy > p:nth-of-type(2){
      color: blue;
    }
  </style>
</head>
<body>
  <div id="ssafy">
    <h2>어떻게 선택 될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
</body>
</html>
```

두번째 단락의 글씨만 파란색으로 변한다.

(3)

nth-child()는 안에 들어있는 자식들(여기서는 p를 자식으로 갖는 div) 기준으로 괄호 안에 있는 숫자에 해당하는 녀석에게 영향을 준다.

nth-of-type()는 정의된 요소(여기서는 p) 중 괄호 안의 숫자 번째에 해당하는 녀석에게 영향을 준다.