## Git 사용법 공부

- git config --global user.name 내용 : 내용 으로 user.name 설정

  git config --global user.email 내용 : 내용 으로 user.email 설정

  한 번 설정하면 쓸 일 없음, 컴퓨터 새로 사면 설정해줘야!

- working directory: 실제 작업 부분 (ex 폴더 내의 파일들)

  git init 으로 설정, 그 directory 안의 파일들을 git으로 관리함

  git으로 관리하기 싫은 파일들(개인정보, 라이브러리 등)은 "특정 함수" 로 설정

- staging area: 임시 저장 부분

  git add 파일 이름 하면 그 파일이 staging area로 이동

  git add . : 디렉토리 내의 모든 파일 staging area로 이동 / 단, 수정된 파일들만 이동

  git status : 깃이 관리중인 파일 표시

  (commit 안 된 파일들 표시, staging area 올라가 있으면 초록색, 아니면 빨간색)

- commit: 업데이트 명시 부분

  git commit -m "메시지 내용" : "메시지 내용" 이라는 변경사항을 commit에 저장

  메시지 내용 적을 때 shift+enter 누르면 칸 내려가 제목과 내용 분리 가능

  ​	git commit 만 입력한 경우

  ​		i를 입력하여 insert 모드

  ​		esc 눌러서 insert모드에서 나옴

  ​		:wq 입력하여 저장하고 나옴

  git log : commit 확인/ 아직 로컬에 존재하는지, 아니면 github와 연동되었는지 확인 가능

  혹시나 맨 끝에 :가 뜨면서 안 나가진다면 q 입력

  git log --oneline : commit 한 줄로 확인

- git remote add origin <url> : origin 이라는 이름을 작성한 url와 연결시킴

  git remote rm origin : 연결되어있는 origin 주소 삭제

  git remote -v : 연결되어있는 사이트 확인

- git push origin master : origin 에서 master(github)로 파일 보내줌: github에서 볼 수 있음

  로컬 저장소에서 원격 저장소로 내용 보내주는 개념

  git push -u origin master : origin에서 master 으로 이동하는 것을 자동으로 저장, 이후 origin master 안 입력해도 가능

- github에 올린 파일 복사해서 내려받는 방법

  - github 내 repository 선택 후 code 버튼 옆의 화살표 눌러 나오는 주소 복사

    이후 git clone <주소> 치면 현재 디렉토리에 다 내려받아짐, repository 포함

  - git clone <주소> . : 현재 폴더 자체에 .git 파일 생성 및 파일 내려받아짐

- git pull : `최초 clone된 것`에서 push 한 것을 내려받을 수 있음: 깃허브의 commit 으로 최신화

  clone-원본 간 상호작용가능

  ***처음 clone한 것에서 바뀐 것이 있어야만 pull할 수 있음!!!***

---

- complete 상황 속 서로 동기화시키기 -> 초기 파일이 존재해야 가능!

  - 같은 파일 내 A'B vs AB' : A'B' 으로 자동으로 완성됨!

  (ex txt 파일 가)

  - branch : 가지 : 분할작업 할 때 설정하는 것

    새 폴더에서 branch 설정할 때 commit 된 파일 하나 이상 존재해야 함!

    git branch : 가지 확인

    git branch -d 가지이름 : 가지이름의 가지 삭제

    git branch 이름 : 이름 의 가지 생성

    git switch 가지이름 : 그 가지이름으로 이동, GUI에서 그 가지 내의 파일만 보임

    git merge 가지이름 : *현재 가지 기준*으로 가지이름 친 가지 파일 통합시킴, 가지는 남아있음