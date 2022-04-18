



[toc]

# Model relationship 2

## 1. ManyToManyField

다대다 관계(M:N) 설정 시 사용하는 모델 필드 (ex) 환자-의사 관계 )

**django 에서는 자동으로 다대다 관계를 설정해주는 모델 필드로 ManyToManyField 명을 사용함**

```python
from django.db import models

class Doctor(models.Model):
    ....
    
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name="....")

# 이런 식으로 사용한다!
```

모델 필드의 RelatedManager 사용하여 관련 개체 조작 가능(추가, 제거 등)

### 1) 요소들

- related_name: 역참조 시 '_set' 안 쓰기 위해 이름 새롭게 정의해주는 역할

- through: 중개 테이블(ManyToManyField 역할) 직접 작성 시 중개 테이블을 나타내는 Django 

  ​                모델을 지정할 수 있음

- symmetrical: 대칭 잠조 / ManyToManyField가 동일한 모델(self) 를 가리키는 정의에서만 사용

  ​						(팔로우 기능 등: 사람이 사람을 팔로우하는 것이니!)

  ​						한 쪽이 다른 한 쪽 참조하면 자동으로 쌍방향 연결되는 것

  ​						기본값은 True

  

### 2) Related Manager

M:N 관계에서는 관련된 두 객체에서 모두 사용 가능!

- add(): 지정된 객체를 관련 객체 집합에 추가 / 이미 관계가 존재하면 복제는 x, 다만 다른 요소 

  ​		   추가하면 가능 ( 환자-의사의 경우 예약날짜 같은 것 추가하면(through 넣어주면) 가능)

- remove(): 관련 객체 집합에서 지정된 객체 제거

- 이 외: create(), clear(), set() 등...찾아보기

---

----

## 2. ManyToManyFIeld 예시

### 1) 좋아요 기능(Like)

- 참고할 사항

  `models.ForeignKey` 랑 `models.ManyToManyField` 동시에 사용하고 참조 모델을 같은 것

  (ex) User) 로 사용 시 둘 중 하나는 꼭 이름을 바꿔야 한다! 즉, related_name 을 사용해야 한다!!

- exist() QuerySet API

  결과가 존재하면 True, 아니면 False 반환: PK가 있는 모델이 QuerySet의 구성원인지 여부를 찾는 가장 효율적인 방법

  

### 2) Profile Page

기존에 배운 것들 활용하여 만들면 됨, 후술할 Follow 기능을 자연스럽게 진행하고자 만드는 것

url은 username 이 들어가도록 설정



### 3) 팔로우 기능(Follow)

- models.py의custom User 에 following 인스턴스 추가

- urls.py 도 추가

- views.py 추가

  ```python
  # 예시
  
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          person = get_object_or_404(get_user_model(), pk=user_pk)
          # 자기 자신은 팔로우 못하게!
          if person != request.user:
              # if request.user in person.followers.all(): 이랑 같음
              if person.followers.filter(pk=request.user.pk).exists():
                  person.followers.remove(request.user)
              else:
                  person.followers.add(request.user)
          return redirect('accounts:profile', person.username)
      return redirect('accounts:login')
  ```

  