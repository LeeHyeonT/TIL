- requirements.txt 가져오기
- 가상환경 만들기
- 터미널에서 가상환경 켜기
- requirements.txt에 있는 것들 다운받기
- 프로젝트 생성하기
- 서버 켜서 돌아가는지 확인하기
- 앱 생성하기
- 생성한 앱 settings.py 에 넣기
  - base.html 사용할 것이기에 template BASE_DIR 설정해주기
- 최상단에 templates 디렉토리 만들어서 base.html 생성하기
- 앱 디렉토리 내에 forms.py, urls.py 생성하기
- 프로젝트 디렉토리 내의 urls.py 작성하기
- 앱 디렉토리 내의 urls.py 작성하기
- 앱 디렉토리 내의 models.py 작성하기
- 앱 디렉토리 내의 forms.py 작성하기
- 앱 디렉토리 내의 views.py 작성하기

- 앱 디렉토리 내에 templates 디렉토리 생성 후 그 안에 또 "앱 이름" 디렉토리 만들어서 그 안에 

  index.html, create.html, detail.html, update.html 만들어 작성하기

- 기본 골격 완성, makemigrations, migrate 하기

  --> 오류 발생! forms.py 에서 ModelForm을 Modelform 이라고 적어서 생긴 문제

  --> 또 오류 발생! models.py 에서 poster_url 을 paoster_url 이라고 적어서 생긴 문제

  --> 또또 오류 발생! 일단 원인은 index.html 안의 

  ` <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>`

  때문에 발생한 듯...아직 미해결

  --> 위의 것 주석 처리하니 movies/ 들어와지고 create 까지 되는데 그 이후  아래 오류가 발생

  --> 오류는 NoReverseMatch 에서 Reverse for 'detail' not found. 인거 보니 detail 쪽의 문제

  --> 오류 해결! 앱 안의 urls.py 안에서 detail 부분을 datail로 기재함....1시간 이상 소요