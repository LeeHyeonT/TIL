# git 활용 2일차

- ignore 기능

  git init 하고 바로 touch .gitignore 만들어줘야 함, 이후 .gitignore 열어서 ignore 할 파일 이름 작성 후 저장(확장자까지!!)

  이미 올라가 있는 자료는 ignore 불가

  https://gitignore.io 들어가서 해당되는 것 체크하고 나오는 것 다 복사해서 .gitignore에 붙여넣기

  (python,windows,visualstudiocode,venv, pycharm)

- git log --oneline --all : 다른 branch 작업 commit 도 확인 가능! but branch 순서까지는 알 수 없음

  이럴 때 git log --oneline --all --graph 쓴다: 순서까지 확인 가능

  merge 후에는 git log --oneline --graph 만 해도 전체  branch구조 보임

- 시간여행

  git reset --hard <commit명 4글자만> : 입력한 commit 까지의 상황으로 돌아감

  git reflog : 전체 log 보여줌, reset 해도 전의 것들도 다 보임

- git switch -c 이름 : 이름 의 branch 를 생성 후 그곳으로 이동함

---

---

# chatbot

- Module: 파일 단위의 파이썬 코드 (a.py 같은 것)

- API : 정보를 받아(url 등) 그 정보 속에서 내가 필요한 부분만 쏘옥 빼 먹는 기능을 가진 상호작용

  Application Programming interface

  각각의 API마다 그 사용방법이 다르기에 설명서 존재, 잘 보고 따라해야!

- 크롤링 : 인터넷 상에서 원하는 정보를 끌어다가 쓰는 기법...