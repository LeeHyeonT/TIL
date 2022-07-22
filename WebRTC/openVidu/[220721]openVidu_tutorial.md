# openVidu

[1. openVidu란?]()

​	[1) 특징]()

[2. openVidu in React (No BE)]()

​	[1) 소개]()

​	[2) 샘플 코드 분석(only 화면)]()

---



## 1. openVidu란?

- 웹이나 모바일 환경에서 화상 통화를 가능하게 하는 [Kurento](https://www.kurento.org/) 기반의 WebRTC 플랫폼
- " 개발자가 쉽고 간편하게 화상 통화 기능을 사용하도록 하는 것 " 이 이 플랫폼의 모토

### 1\) 특징

- 플랫폼에 구애받지 않음

  Chrome, Firefox Safari, Opera, Edge, Android, iOS 모두 사용 가능

- custom 하기 어렵지 않음

  우선 기본 tutorial 가지고 기본적인 기능 쉽게 확인 가능

  이후 자체 api들을 이용하여 여러 기능들을 손쉽게 사용 가능

  api들에 대한 분석은 추후에 진행할 예정

- 화상 미팅에 필요한 기본적인 기능들은 다 가지고 있음

  카메라를 이용한 얼굴 보이기, 채팅, 화면 공유 등

- docker을 활용하여 openVidu 서버를 생성함

  아무래도 openVidu의 모토 때문에 서버 구축도 상대적으로 쉬운 docker로 진행하는듯



## 2. openVidu in React (No BE)

### 1) 소개

![image-20220721142634427](../../../../../AppData/Roaming/Typora/typora-user-images/image-20220721142634427.png)

총 세 가지 부분에서 작업이 이루어짐

- openVidu-Browser

  React 라이브러리를 활용하여 실제로 사용자에게 보여지는 부분

  이번에 작성되는 코드는 이 부분에서만 작용하게됨

- openVidu-Server

  Kurento Media Server 를 다루기 위한 java application

  java application? 이것의 정확한 뜻이 뭘까?

- Kurento Media Server

  미디어(여기서는 화상 미팅) 전송을 위한 서버

  

### 2) 샘플 코드 분석 (only 화면)

- `App.js`

  화상 미팅을 진행하는 데에 있어 기본적인 setting 을 담담하는 부분

  - ```javascript
    import { OpenVidu } from 'openvidu-browser';
    ```

    browser 공간에서 openvidu를 사용하기 위하여 `npm package` 인 `openvidu-browser` 를 사용

  - ```javascript
    this.state = {
        mySessionId: 'SessionA',
        myUserName: 'Participant' + Math.floor(Math.random() * 100),
        session: undefined,
        mainStreamManager: undefined,
        publisher: undefined,
        subscribers: [],
    };
    ```

    사용할 데이터들을 모아놓은 공간

    `sessionId`, `username,` `session` : 말 그대로 !

    `mainStreamManager` : 가장 큰 화면을 누가 다루고 있는지 

    ​										--> (화면공유하고 있지 않을 때) 대부분 발언하는 사람을 여기에 넣음

    `publisher` : 미팅 만든 사람

    ​						--> 프로젝트에서는 채널 관리자

    `subscribers` : 미팅 참여한 사람

    ​						--> 프로젝트에서는 채널 참가자

  - ```javascript
    this.OV = new OpenVidu();
    
    this.setState({
        session: this.OV.initSession(),
        }, () => {
            
        }
    );
    ```

    위에서 import 해온 것을 이용하여 새로운 화상 미팅 session을 생성하는 코드

    `this.setState` : 위의 `this.state` 내부에 정의해놓은 데이터의 값을 set 시키는 코드

    여기서는 `session` 값을 set 시켜줌

  - ```javascript
    var mySession = this.state.session;
    
    mySession.on('streamCreated', (event) => {
        var subscriber = mySession.subscribe(event.stream, undefined);
    
        var subscribers = this.state.subscribers;
    
        subscribers.push(subscriber);
    
        this.setState({
            subscribers: subscribers,
        });
    });
    
    mySession.on('streamDestroyed', (event) => {
        event.preventDefault();
        
        this.deleteSubscriber(event.stream.streamManager);
    });
    
    mySession.on('exception', (exception) => {
        console.warn(exception);
    });
    ```

    subscribers를 정의하는 부분

    전제적인 흐름: 생성된 session 에 현재 들어와 있는 인원을 파악하여 그들을 `state`의 `subscribers` 						  array에 넣어주는 것

    화상 미팅이 종료된 경우 `subscribers` array를 비워줌

    기타 다른 오류들이 발생하는 경우 console 창에 띄워줌

    `streamManager` 는 위의 `mainStreamManager` 를 받아서 쓰는 변수

  - ```react
    {this.state.subscribers.map((sub, i) => (
        <div key={i} className="stream-container col-md-6 col-xs-6">
            <UserVideoComponent streamManager={sub} mainVideoStream={this.handleMainVideoStream} />
        </div>
    ))}
    ```

    위의 `subscribers` 관련하여 state 내 값이 변동될 때마다 react 에서 비동기적으로 확인 가능하도록 만들어주는 코드

- `App.css`

  말 그래도 css 부분.... 

  우리는 이렇게  파일로 만들 것은 아니기에 무시해도 되는 파일

- `UserVideoComponent.js`

  `app.js` 로 import 하여 react 내 html 파트에 사용되는 파일

  실질적으로 video가 어떻게 보이는 지에 대한 구성으로 이루어짐