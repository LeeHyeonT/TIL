# 0207_workshop

- index.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
  rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
  <!-- 1. Nav -->
  <nav class="fixed-top bg-dark d-flex justify-content-between align-items-center">
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>
    <ul class="d-flex align-items-center mb-0">
      <li class="mx-3"><a class="text-white text-decoration-none" href="#">Home</a></li>
      <li class="mx-3"><a class="text-white text-decoration-none" href="#">Community</a></li>
      <li class="mx-3"><a class="text-white text-decoration-none" href="#">Login</a></li>
    </ul>
  </nav>

  <!-- 2. Header -->
  <header class="d-flex flex-column justify-content-center align-items-center text-white fw-bold">
      <div class="display-2">Cinema</div>
      <div class="display-2">Community</div>
      <a class="btn btn-primary mt-5" m href="#">Let's Go</a>
  </header><br><br><br>

  <!-- 3. Section -->
  <section>
    <h2 class="d-flex justify-content-center my-5">Used Skills</h2>
    <article class="d-flex justify-content-evenly">
      <div>
        <img src="images/web.png" alt="Web Image">
        <p class="d-flex justify-content-center">Web</p>
      </div>
      <div>
        <img src="images/html5.png" alt="HTML5 Image">
        <p class="d-flex justify-content-center">HTML5</p>
      </div>
      <div>
        <img src="images/css3.png" alt="CSS3 Image">
        <p class="d-flex justify-content-center">CSS3</p>
      </div>
    </article>
  </section>

  <!-- 4. Footer -->
  <footer class="fixed-bottom d-flex bg-primary text-white justify-content-center align-items-center h-40">
    <p class="d-flex my-auto">HTML & CSS project. Created by LeeHyeonT</p>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
</body>
</html>
```

- style.css

```css
import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR');

/* 아래의 코드는 수정하지 마세요. */
body {
  height: 3000px;
  margin: 0;
  font-family: 'Noto Sans KR', sans-serif;
}

nav {
  height: 80px;
}

nav img {
  height: 80px;
}

header {
  height: 700px;
  background-image: url('images/header.jpg');
  background-size: cover;
}

section > h2 {
  font-size: 3rem;
}

section img {
  width: 300px;
}

footer {
  height: 60px;
}


/* 추가적으로 작성하고 싶은 순수 CSS 코드가 있다면 해당 주석 아래에 작성해 주세요. */
footer{
  height:40px;
}
```

