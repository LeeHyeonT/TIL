# Docker

[1. Docker?](#1-docker)

[2. 설치](#2-설치)

[3. 간단한 실행](#3-간단한-실행)

# 1. Docker?

- container 기술 및 관리를 단순화하여 활용하기 위한 도구

  - container?

    A standardized unit of sortware

    A package of code and dependencies to run that code (NodeJS code + NodeJs runtime....)

  container에 software unit, package with code, code dependencies를 보관할 수 있음

  이후 어느 곳에서든지 이 container를 꺼내 동일하게 실행시킬 수 있음

- independent, standardized "application package"

  --> 따로따로 버전 관리에 용이하다!

- Virtual Machine 와의 비교

  - Virtual Machine의 문제

    - Overhead : 컴퓨터 CPU, 드라이브 공간 낭비로 인한 컴퓨터 성능 저하 문제
    - 계속 새로운 환경을 구성해줘야함 : 반복작업으로 인한 귀찮음

  - Container를 사용하며 얻는 이점

    - Docker Engine 이용 : 운영 체제의 매우 가벼운 버전

      이 위에 container를 생성하여 사용하기에 컴퓨터 성능 저하 문제 x

    - 만든 것을 공유 및 재구축하기 용이함

## 2. 설치

각 운영체제에 맞는 것을 설치

Docker Desktop, Docker ToolBox 두 가지 종류로 사용 가능한데 웬만하면 Docker Desktop으로 가는게 좋다

- Windows 10 Pro, Education, Enterprise : Hyper-V 를 통한 Install Docker Desktop 하지만 아래 방법도 가능

- windows 10 Home : 가상환경을 지원하는 경우 WSL를 통한 Install Docker Desktop

- WSL을 통한 Docker 설치 방법

  - `windows powershell`  을 관리자 권한으로 실행하여 다음 코드 입력

    ```powershell
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```

    기본적인 WSL 설치하는 과정

  - Windows 버전 확인

    - x64 시스템의 경우: **버전 1903** 이상, **빌드 18362** 이상
    - ARM64 시스템의 경우: **버전 2004** 이상, **빌드 19041** 이상

  - 다음 코드 입력

    ```powershell
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
  
  - WSL2 버전을 위한 리눅스 커널 업데이터 설치
  
    - `this update only applies to machines with the windows subsystem for linux` 오류가 발생할 시
  
      컴퓨터를 재부팅한다!
  
  - WSL2 버전으로 업그레이드를 위한 코드 입력
  
    ```powershell
    wsl --set-default-version 2
    ```
  
  - Linux 베포할 운영체제 선택 후 설치
  
    기본적으로 Ubuntu를 많이 설치함
  
    설치 후 간단한 사용자 / 비밀번호 등록 
  
    여기까지 진행하면 Docker을 깔 준비가 된 것!
  
  - 각 운영체제에 맞는 Docker 설치파일 다운로드 후 설치

 ## 3. 간단한 실행

- Docker 을 실행하기 위해서는 어떠한 언어로 만들어진 코드와 `Dockerfile` 이 필요함

- `Dockerfile` 안에는 어떠한 환경에서 실행하는지, 어느 위치의 파일을 실행하는지 등등의 정보가 담겨있음

- 명령어 입력 창에 `docker build .` 입력 

  이후 `docker run -p 포트번호:포트번호 id` 입력

  - 포트번호 : 우리가 연결하려는 포트의 번호

    기본 예시에서는 `app.listen(3000);` 을 통해 포트 3000으로 연결하려고 하기에 포트번호에 3000 입력

  - id : `docker build .` 해서 나오는 image의 id값

  이 과정까지 거치면 `localhost:3000` 주소 연결 가능!

- 실행 멈추기

  - 새로운 명령어 입력 창 생성 후 `docker ps` 입력

    여기서 우측 하단에 나오는 이름을 가지고 `docker stop 이름` 입력

