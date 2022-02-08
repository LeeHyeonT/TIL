# 0208_workshop

## 1. �⺻ �׸��� ���̾ƿ�

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice1</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 1</h1>
      </div>
    </div>
    
    <!-- 1. -->
    <div class="row">
      <div class="item col-4">
        <p>1</p>
      </div>
      <div class="item col-4">
        <p>2</p>
      </div>
      <div class="item col-4">
        <p>3</p>
      </div>
    </div>

    <!-- 2. -->
    <div class="row">
      <div class="item col-6">
        <p>1</p>
      </div>
      <div class="item col-6">
        <p>2</p>
      </div>   
    </div>

    <!-- 3. -->
    <div class="row">
      <div class="item col-3">
        <p>1</p>
      </div>  
      <div class="item col-6">
        <p>2</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div>
    </div> 
    
    <!-- 4. -->
    <div class="row">
      <div class="item col-2">
        <p>1</p>
      </div>
      <div class="item col-7">
        <p>2</p>
      </div>
      <div class="item col-3">
        <p>3</p>
      </div> 
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```



## 2. ������ �׸���

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice2</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 2</h1>
      </div>
    </div>

    
    <!-- 1. -->
    <div class="row">
      <div class="item col-4 col-sm-2">
        <p>576px �̸� 4 <br> 576px �̻� 2</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px �̸� 4 <br> 576px �̻� 5</p>
      </div>
      <div class="item col-4 col-sm-5">
        <p>576px �̸� 4 <br> 576px �̻� 5</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <div class="item col-1 col-md-2">
        <p>768px �̸� 1 <br> 768px �̻� 2</p>
      </div>
      <div class="item col-3 col-md-3">
        <p>768px �̸� 3 <br> 768px �̻� 3</p>
      </div>
      <div class="item col-4 col-md-3">
        <p>768px �̸� 4 <br> 768px �̻� 3</p>
      </div>
      <div class="item col-1 col-md-2">
        <p>768px �̸� 1 <br> 768px �̻� 2</p>
      </div>
      <div class="item col-3 col-md-2">
        <p>768px �̸� 3 <br> 768px �̻� 2</p>
      </div>
    </div>


    <!-- 3. -->
    <div class="row">
      <div class="item col-4 col-sm-3 col-md-6">
        <p>576px �̸� 4 <br> 768px �̸� 3 <br> 768px �̻� 6</p>
      </div>
      <div class="item col-6 col-sm-3 col-md-6">
        <p>576px �̸� 6 <br> 768px �̸� 3 <br> 768px �̻� 6</p>
      </div>
      <div class="item col-2 col-sm-6 col-md-12">
        <p>576px �̸� 2 <br> 768px �̸� 6 <br> 768px �̻� 12</p>
      </div>
    </div>


    <!-- 4. -->
    <div class="row">
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px �̸� 12 <br> 768px �̻� 4 <br> 1200px �̻� 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-2">
        <p>768px �̸� 12 <br> 768px �̻� 4 <br> 1200px �̻� 2</p>
      </div>
      <div class="item col-12 col-md-4 col-xl-12">
        <p>768px �̸� 12 <br> 768px �̻� 4 <br> 1200px �̻� 12</p>
      </div>
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```



## 3. �׸��� ��ȭ

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>practice3</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 3</h1>
      </div>
    </div>

    <!-- 1. -->
    <div class="row">
      <div class="item col-4">
        <p>item1</p>
      </div>
      <div class="item col-8 col-md-4 offset-md-4">
        <p>item2</p>
      </div>
    </div>


    <!-- 2. -->
    <div class="row">
      <div class="item col-4 col-md-4 col-lg-5 offset-md-4 offset-lg-7">
        <p>item1</p>
      </div>
      <div class="item col-4 col-lg-8 offset-4 offset-md-0 offset-lg-2">
        <p>item2</p>
      </div>
    </div>
    

    <!-- 3. -->
    <div class="row">
      <div class="item col-12 col-md-3">
        item1
      </div>
      <div class="item col-12 col-md-9">
        <div class="row">
          <div class="item col-6 col-lg-3">item2</div>
          <div class="item col-6 col-lg-3">item3</div>
          <div class="item col-6 col-lg-3">item4</div>
          <div class="item col-6 col-lg-3">item5</div>
        </div>
      </div>
    </div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```

