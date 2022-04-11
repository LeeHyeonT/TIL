

[toc]

# Authentication System 1

## 1. The Django Authentication System

Django에서는 친절하게도 project 내부의 `settings.py` 안에 이미 auth 시스템 모듀을 갖춰놓음

- django.contrib.auth: 인증 framework 핵심과 기본 모델
- django.contrib.contenttypes: 사용자가 생성한 모델에 권한 부여

인증(Authentication), 권한(authorization) 부여를 함께 처리하는 방식

새롭게 accounts 라는 앱 생성하여 진행

`python manage.py startapp accounts`

--> 앱 이름이 accounts 일 필요는 없지만 나중에 편리하므로 웬만하면 accounts 로 하자!!!

앱 생성 후 settings.py 에 등록, url 설정

----

----

## 2. Cookie, Session

### 1) 개념

- HTTP: Hyper Text Transfer Protocol: HTML 파일 등의 리소스들을 가져올 수 있도록 해주는 규약
- HTTP 특징
  - 비연결지향(conntectionless): 서버는 요청에 대한 응답을 보낸 후 **연결을 끊음!**
  - 무상태(stateless): 연결을 끊으면 상태 정보가 유지되지 않음: 클라이언트-서버 간 소통하는 것의 독립성

***이러한 특징을 이겨내고 클라이언트-서버의 지속적인 관계를 유지하기 위해 Cookie, Session이 존재!***

- Cookie: 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

  ​			: 해당 웹사이트의 서버를 통해 사용자 컴퓨터에 저장되는 작은 기록 정보 파일

  - Cookie 이용: HTTP Cookie는 동일한 브라우저에서 요청이 들어왔는지 판단할 때 주로 사용

    ​					 : 사용자의 로그인 상태를 유지할 수 있음

  요청한 웹 페이지에서 쿠키 받아 저장하고 클라이언트가 같은 서버에 재 요청할 시 요청과 함께 쿠키도 함께 전송! 쿠키는 저장되어 계속 왔다갔다 하는 형태

  - Cookie 사용 목적
    - 세션 관리: 로그인, 장바구니, 팝업 등
    - 개인화: 사용자 설정
    - 트래킹: 사용자의 행동을 기록 및 분석
  - Cookie lifetime 
    - Session cookies: 현제 세션이 종료되면 삭제
    - Persistent cookies: 정해놓은 일정 기간이 지나면 삭제

- Session: 사이트와 특정 브라우저 사이의 상태(state) 를 유지시키는 것!

  클라이언트가 서버에 접속할 시 서버가 발급하는 **session id** 를 클라이언트가 쿠키에 저장

  - Session in Django

    settings.py의 MIDDLEWARE 을 통해 구현, 기본값으로 database-backed sessions 저장 방식

    (MIDDLEWARE? : HTTP 요청과 응답 처리 중간에서 작동 / 데이터 관리, 앱 서비스, 인증 및 API 관리 담당)

    특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 을 알아냄

----

----

## 3. LogIn

built-in forms 를 이용하여 구현

`from django.contrib.auth import login` : views.py 에서 login 함수를 정의할 것이기에

- `from django.contrib.auth import login as auth_login` 처럼 이름 재정의해서 사용하는 편!

- ` from django.contrib.auth.forms import AuthenticationForm` 

이 두 가지 사용하여 login 함수 만든다! 형태는 CRUD 방식 그대로!

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 전에 한 CRUD 방식과 고대~로 같은 방식!!
```

----

----

## * Authentication data in templates *

로그인 되어있는 유저 정보 출력할 때 `{{ user }}` 이렇게 표현할 수 있는데 이게 가능한 이유는 settings.py 에 있는 context processors 덕분! 거기서 ....auth 부분의 역할

---

----

## 4. LogOut

session을 delete 하는 로직!

`from django.contrib.auth import logout` 이용하는데 앞서 login 과 마찬가지로 이름 바꿔 사용

- `from django.contrib.auth import logout as auth_logout`

```python
from django.views.decorators.http import require_POST
form django.contrib.auth import logout as auth_logout

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

---

----

## 5. 로그인 사용자에 대한 접근 제한

두 가지 방식으로 가능!

\>  **is_authenticated** attribute

User model의 속성값 중 하나: User 인스턴스 존재하면 True, Anonymous User면 False

permission 과는 관련 없고 단지 아이디 있는지 없는지만 확인

base template 에 `{% if request.user.is_authenticated %}` ~~ `{% else %}` ~~ `{% end if %}`

views.py 의 login 함수에 `if request.user.is_authenticated:`

views.py 의 logout 함수에 `if request.user.is_authenticated:`

필요한 template 에 base template 에 한 것처럼 진행



\>  **login_required** decorator 

사용자가 로그인되어있지 않으면 `settings.LOGIN_URL` 에 설정된 절대 경로로 redirect

--> 설정된 기본값은 **/accounts/login/**

사용자가 로그인되어 있으면 정상적으로 view 함수 실행

- `from django.contrib.auth.decorators import login_required` 이용

인증 성공 시 redirect 경로는 "next" 라는 쿼리 문자열 매개 변수에 저장됨 (..../next=......)

---> "next" 값을 이용하기 위해 return 값을

` return redirect(request.GET.get('next') or 'articles:index')` 처럼 or 이용하여 변경

또한 **form의 action값을 비워놔** 현재 URL 로 요청을 보내야 함!



### * @login_required 와 @required_POST 의 충돌 *

login_required 진행하는 방식이 GET 방식으로 요청되어 진행하기에 뒤에 있는 required_POST 는 진행하지 못하고 405 ERROR 뜸

따라서 login_required 는 GET method request 를 처리할 수 있는 함수에서만 사용해야함!

----

----

# Authentication System 2

## 1. 회원가입

`UserCreationForm` 사용: username, password1, password2 의 3개의 field 가짐

- `from django.contrib.auth.forms import UserCreationForm` 

방법은 CRUD 에서 C 방법과 동일!

## 2. 회원탈퇴

방법은 CRUD 에서 D 방법과 동일!

혹여나 탈퇴하면서 해당 유저의 세션 데이터도 함께 지울 경우

```python
request.user.delete()
auth_logout(request)
```

처럼 **탈퇴처리 후 로그아웃 순** 으로 처리해야함!

## 3. 회원정보 수정

`UserChangeForm` 사용: 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- `from django.contrib.auth.forms import UserChangeForm`

방법은 CRUD 에서 U 방법과 동일!

하지만 `UserChangeForm` 을 그대로 사용하면 일반 사용자가 접근해서는 안될 fields 까지 모두 수정이 가능해짐...

따라서 `UserChangeForm` 을 커스텀하여 사용해야함!

--> 앱에서 forms.py 만들어

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('넣고', '싶은', '것들')
```

이런 식으로 class 만들어 사용해야함!

update 과정이니 class 변수로 instance 값 받아줘야하는 것 주의! 여기서는 `instance=request.user`

----

----

## 4. 비밀번호 변경

`PasswordChangeForm` 이용: 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함

이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 `SetPasswordForm` 을 상속받는 class

- `from django.contrib.auth.forms import PasswordChangeForm`

방법은 CRUD 의 C 와 동일! U 가 아닌 이유는 비밀번호는 DB에 저장하지 않기 때문이다!

혹여나 비밀번호 변경 후 세션이 무효화되는 것(로그아웃 되는 것)을 방지하려면

- `from django.contrib.auth import update_session_auth_hash` 이용!

  ```python
  form.save()
  update_session_auth_hash(request, form.user)
  return redirect....
  ```

  처럼 사용!

----

----

## 기타

venv 생성 후 디렉토리 이름 바꿨다면?

1) `rm -rf ./ venv` 로 기존 venv 삭제
2) 다시 venv 깔고
3) requirements.txt 에 있는 것들 다운로드