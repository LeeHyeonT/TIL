# 0203_workshop

## 1. img tag

```html
<img src="c:\Users\Windows_10\Desktop\TIL\ssafy/image/my_photo.png" alt="ssafy">
```



## 2. ���� ���

(a) : ���� ���

(b) : ��� ���

```html
<img src="../img/my_photo.png" alt="ssafy">
```



## 3. Hyper Link

```html
<a href="https://ssafy.com">
  <img src="ssafy/image/my_photo.png" alt="ssafy">
</a>
```



## 4. ������

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
    <h2>��� ���� �ɱ�?</h2>
    <p>ù��° �ܶ�</p>
    <p>�ι�° �ܶ�</p>
    <p>����° �ܶ�</p>
    <p>�׹�° �ܶ�</p>
  </div>
</body>
</html>
```

ù��° �ܶ� �� �۾��� ���������� ���Ѵ�. 

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
    <h2>��� ���� �ɱ�?</h2>
    <p>ù��° �ܶ�</p>
    <p>�ι�° �ܶ�</p>
    <p>����° �ܶ�</p>
    <p>�׹�° �ܶ�</p>
  </div>
</body>
</html>
```

�ι�° �ܶ��� �۾��� �Ķ������� ���Ѵ�.

(3)

nth-child()�� �ȿ� ����ִ� �ڽĵ�(���⼭�� p�� �ڽ����� ���� div) �������� ��ȣ �ȿ� �ִ� ���ڿ� �ش��ϴ� �༮���� ������ �ش�.

nth-of-type()�� ���ǵ� ���(���⼭�� p) �� ��ȣ ���� ���� ��°�� �ش��ϴ� �༮���� ������ �ش�.