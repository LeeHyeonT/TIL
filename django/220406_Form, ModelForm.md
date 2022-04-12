[toc]

[1. Form](#1. Form)

# 1. Form

Django Form 을 이용하여 받아오는 데이터의 유효성 검증을 쉽게 할 수 있음:

- rendering 데이터 준비 및 재구성
- 데이터에 대한 HTML forms 생성
- 클라이언트로부터 받은 데이터 수신 및 처리

를 처리해준다!



앱 디렉토리 안에 `forms.py` 생성하여 

- `from django import forms` 이용하여  Form 선언!

```python
from django import forms

class ...Form(forms.Form)
# forms 라이브러리에서 파생된 Form 클래스를 상속받아 사용함
```

이후 views.py 내부 함수에서 위의 ...Form 사용할 부분 수정, html 파일에 나오게끔 설정



## - Form rendering options (Form이 어떻게 보여질 것인가)

- as_p(): 각 필드가 단락(p 태그) 으로 감싸져서 rendering

- as_ul(): 각 필드가 목록(li 태그) 으로 감싸져서 rendering

  `<ul>` 태그는 직접 작성해야 함!

- as_table(): 각 필드가 테이블(tr 태그) 행으로 감싸져서 rendering

  `<table>` 태그는 직접 작성해야 함!



## - Django의 HTML input 요소 표현 2가지

- Form fields

  후에 기술할 ModelForm에서 `fields = '__all__'` 했을 때의 그 fields

- Widgets

  GET / POST 딕셔너리에서 데이터 추출!

  Form fields에 할당 됨

----

----

# 2. ModelForm

Django에서는 Model을 통해 Form Class를 만들 수 있는 ModelForm 이라는 Helper를 제공해줌

```python
from django import forms
from .models import ...

class ...Form(forms.ModelForm):
    
    class Meta:
        model = ...
        fields = ...
        # exclude = ...
# fields와 exclude는 동시 사용 불가능! fields는 어떤 것들을 나타낼 것인지, exclude는 어떤 것들을 제외하고 나머지 것들을 나타낼 것인지 표현
```

위에 표현한 Meta class: Model의 정보를 작성하는 곳 / ModelForm이 사용할 Model을 구성함

**Meta 데이터: 데이터에 대한 데이터** 라는 의미이므로 class 명칭을 Meta 라고 한 것!



- `is_valid()` method

  views.py 안의 함수를 위에서 만든 ModelForm 을 이용하여 수정 후 유효성 검사를 할 수 있는 method

  데이터가 유효한지에 대한 여부를 boolean으로 반환

- `save()` method

  Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장하는 method

  ModelForm의 경우 ModelForm의 sub클래스는 기존 모델의 인스턴스를 **instance** 라는 키워드로 받아들일 수 있음!

  - 이게 제공되는 경우 `save()` 는 해당 인스턴스를 수정 (CRUD에서 U)
  - 제공되지 않는 경우 `save()` 는 지정된 모델의 새 인스턴스를 만듦(CRUD에서 C)

- forms.py 위치

  아무데나 두어도 상관없으나 앱 디렉토리/forms.py 가 되는 것을 권장함!(관리하기 편하잖아!)



## * widget 활용하기 *

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    label='제목',
    widget=forms.TextInput(
    	attrs={
            'class': my-title',
            'placeholder': 'Enter the title',
        }
    ),
)
    class Meta:
        model = Article
        fields = '__all__'
```

이런 식으로 **model 내 field 하나씩** 꺼내서 **그 안에 widget** , **그 안에 attrs** 하는 식으로 꾸미는 방식을 추천함!!

----

----

# 3. Rendering fields manually

## 1) Rendering fields manually

field 하나하나 꺼내서 하나하나 쓰는 방식

`{{ form.title.errors }}`

`{{ form.title.label_tag }}`

`{{ form.content.errors }}`

`{{ form.content.label_tag }}`

이런 식!

## 2) Looping over the form's fields (using {% for %})

for문 이용하여 묶어서 표현하는 방식

`{% for field in form %}`

​	`{{ field.errors }}`

​	`{{ field.label_tag}}`

`{% end for %}`

이런 식!



# ** Bootstrap 적용시키기 **

**form-control** 클래스를 적용시켜 사용! 

- base.html 에 이미 cdn은 넣어놓은 상태이므로 widget 에서 각각의 field 꾸밀 때 

  `'class': 'form-control'`꼭 넣어준다!

이후 다른 보여줄 html 파일들에 div 등 이용하여 원래 하던 것처럼 bootstrap 사용하면 된다!



- cdn을 넣어놓지 않은 경우 `pip install django-bootstrap-v5` 하여 다운받고 

settings.py 의 INSTALLED_APPS 에 'bootstrap5' 등록시키고

(pip freeze > requirements.txt 하여 새로 받은 것 동기화시키고)

base.html에 

`{% load bootstrap5 %}`

...

`{% bootstrap_css %}`

...

`{% bootstrap_javascript %}`

작성하면 된다!

이후 나머지 html 파일들에도 `{% load bootstrap5 %}` 는 꼭 넣어주고 

django-bootstrap 에서 제공하는 다양한 tags 이용하여 꾸며주면 된다!