[toc]

# Python 을 활용한 데이터 수집 II

## 1. 목표

- Python 기초 문법 실습 
- 데이터 구조에 대한 분석과 이해
- 요청과 응다벵 대한 이해
- API의 활용과 문서 분석

## 2. 준비사항

1) 사용 데이터
   - TMDB API(https://developers.themoviedb.org/3)
   - 영화 정보 및 API 서비스
2) 개발언어/프로그램
   - Python 3.9 이상
3) 필수 라이브러리
   - requests



## 3. 요구사항

### A. 인기 영화 조회

#### 전체 코드

```python
import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    parameter = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'region': 'KR',
        'language': 'KO'
    }
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL + path, params = parameter).json()
    datas = response['results']

    return len(datas)

```



#### 코드 분석

```
import requests
```

`requests` 모듈을 불러옵니다.  웹 사이트의 정보를 가지고 오고 싶을 때 사용합니다. 여기서는 `.get()` 메소드와 `.json()` 메소드를 사용하여 웹 사이트 정보를 json 파일 형태로 가지고 올 예정입니다. 

```python
def popular_count():
    pass
```

`popular_count` 라는 함수를 정의합니다.

```python
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
parameter = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'region': 'KR',
        'language': 'KO'
    }
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter 내의 값은 path값에 따라 달라집니다. parameter 값에서 required 는 무조건 들어가야하고 optional은 넣어도, 넣지 않아도 됩니다. 

```python
response = requests.get(BASE_URL + path, params = parameter).json()
datas = response['results']

return len(datas)
```

`response` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

`datas` 를 `response ` dictionary 안의 'results' key 의 value값들로 정의합니다. 영화 정보가 담긴 list값이 될 것입니다.

`datas` 의 길이를 반환합니다. 



#### 피드백

- requests 모듈을 이용해서 웹 페이지 내 정보를 끌어오는 것이 신기했다.
- api 주소에 따라서 필요한 값들이 달라진다.

---

---

### B. 특정 조건에 맞는 인기 영화 조회 I 

#### 전체 코드

```python
import requests
from pprint import pprint


def vote_average_movies():
    pass 
    # 여기에 코드를 작성합니다.  
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    parameter = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'region': 'KR',
        'language': 'KO'
    }
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL + path, params = parameter).json()
    datas = response['results']
    data_over_8 = []
    for data in datas:
        if data['vote_average'] >= 8:
            data_over_8.append(data['title'])
    
    return data_over_8
```



#### 코드 분석

```python
import requests
from pprint import pprint
```

`requests` 모듈과 `pprint` 모듈을 불러옵니다.

```python
def vote_average_movies():
    pass
```

`vote_average_movies` 라는 함수를 정의합니다. 

```
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
parameter = {
'api_key': '1d782b494774c8b795a68a320100ebdd',
'region': 'KR',
'language': 'KO'
}
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter 내의 값은 path값에 따라 달라집니다. 

```
response = requests.get(BASE_URL + path, params = parameter).json()
datas = response['results']
data_over_8 = []
for data in datas:
	if data['vote_average'] >= 8:
		data_over_8.append(data['title'])

return data_over_8
```

`response` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

`datas` 를 `response ` dictionary 안의 'results' key 의 value값들로 정의합니다. 영화 정보가 담긴 list값이 될 것입니다.

`data_over_8` 를 list 형식으로 정의합니다. vote_average 가 8 이상인 영화의 title값을 담을 예정입니다.

`datas` 리스트 내의 값들에 대해 반복문을 정의합니다.

만약 리스트 내의 값(dictionary 형식) 의 'vote_average' key의 value값이 8 이상이면 리스트 내의 값의 'title' key의 value값을 `data_over_8`  에 추가합니다.

`data_over_8` 을 반환합니다.



#### 피드백

- requests 모듈을 사용할 때 다른 파일에서 쓴 것과 같은 주소를 사용한다면 그걸 그대로 가지고 오는 방법은 없는지 궁금하다.
- response 값이 복잡하게 구성되어있기에 천천히 훑어봐야한다.

---

---

### C. 특정 조건에 맞는 인기 영화 조회 II 

#### 전체 코드

```python
import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.  
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    parameter = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'region': 'KR',
        'language': 'KO'
    }
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL + path, params = parameter).json()
    datas = response['results']
    vt_avg_list = []
    for data in datas:
        vt_avg_list.append(data['vote_average'])
    vt_avg_list.sort(reverse = True)
    
    vt_avg_5_movie_list = []
    for data in datas:
        for idx in range(5):
            if data['vote_average'] == vt_avg_list[idx]:
                vt_avg_5_movie_list.append(data)

    return vt_avg_5_movie_list
```



#### 코드 분석

```python
def ranking():
    pass 
```

`ranking`이라는 함수를 정의합니다.

```python
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
parameter = {
'api_key': '1d782b494774c8b795a68a320100ebdd',
'region': 'KR',
'language': 'KO'
}
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter 내의 값은 path값에 따라 달라집니다. 

```python
response = requests.get(BASE_URL + path, params = parameter).json()
datas = response['results']
vt_avg_list = []
for data in datas:
	vt_avg_list.append(data['vote_average'])
vt_avg_list.sort(reverse = True)
```

`response` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

`datas` 를 `response ` dictionary 안의 'results' key 의 value값들로 정의합니다. 영화 정보가 담긴 list값이 될 것입니다.

`vt_avg_list` 를 리스트의 형태로 정의합니다. 영화들의 vote_average들을 저장할 예정입니다.

`datas` 리스트 내의 값들에 대해 반복문을 정의합니다.

`vt_avg_list` 에 `datas` 의 성분인 `data` dictionary의 'vote_average' key 에 해당하는 value값을 추가합니다.

`vt_avg_list` 리스트 안의 값들을 내림차순으로 정렬합니다.

```python
vt_avg_5_movie_list = []
for data in datas:
	for idx in range(5):
		if data['vote_average'] == vt_avg_list[idx]:
            if data not in vt_avg_5_movie_list:
				vt_avg_5_movie_list.append(data)
            else:
                continue

return vt_avg_5_movie_list
```

`vt_avg_5_movie_list` 를 리스트의 형태로 정의합니다. 평점 1~5등까지의 영화들의 정보가 저장될 예정입니다.

`datas` 리스트 내의 값들에 대해 반복문을 정의합니다.

그 반복문 안에 5번 반복하는 반복문을 정의합니다.

만약 `data` dictionary의 'vote_average' key 에 해당하는 value값이 `vt_avg_list` 리스트의 첫번째~다섯번째 값에 해당한다면 `vt_avg_5_movie_list` 에 그 `data` 를 추가합니다. 그럼 평점이 1~5등인 영화의 데이터가 리스트의 요소로 저장될 것입니다.

하지만 1~5등 평점 중 중복된 값이 있으면 같은 영화 `data` 가 두 번 들어갈 수 있기에 만약 `data` 가 `vt_avg_5_movie_list`  에 들어있지 않을 때만 `data` 를 `vt_avg_5_movie_list`  에 추가합니다.

`vt_avg_5_movie_list` 값을 반환합니다.



#### 피드백

- 상위 5개 평점 중 같은 값이 있는 경우도 따져야해서 헷갈렸다.

---

---

### D. 특정 영화 추천 영화 조회 

#### 전체 코드

```python
import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # 1. URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    parameter = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'query': title,
        'region': 'KR',
        'language': 'KO'}
    
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL + path, params = parameter).json()
    try:
       id_data = response['results'][0]['id']
    except IndexError:
        return None 
    

    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 = '/movie/'+ str(id_data) + '/recommendations'
    parameter2 = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'language': 'KO'}
    
    response2 = requests.get(BASE_URL2 + path2, params = parameter2).json()
    datas2 = response2['results']
    recmd_movie_title = []
    for data in datas2:
        recmd_movie_title.append(data['title'])
    
    return recmd_movie_title
```



#### 코드 분석

```python
def recommendation(title):
```

`recommendation` 이라는 함수를 정의합니다. 이 함수는 `title` 을 변수로 갖습니다.

```python
BASE_URL = 'https://api.themoviedb.org/3'
path = '/search/movie'
parameter = {
    'api_key': '1d782b494774c8b795a68a320100ebdd',
    'query': title,
    'region': 'KR',
    'language': 'KO'}
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter 내의 값은 path값에 따라 달라집니다. 

```python
response = requests.get(BASE_URL + path, params = parameter).json()
try:
    id_data = response['results'][0]['id']
except IndexError:
    return None
```

`response` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

올바르지 않은 영화 제목으로 검색하여 id가 존재하지 않는 경우 None 을 출력하기 위한 try-except 문입니다. 정상적인 영화 제목이 검색된다면 `response['results']` 값이 존재하여 index 0번을 찾아가는 `response['results'][0]` 값이 존재하겠지만 올바르지 않은 제목으로 검색한다면 response 값 자체가 존재하지 않아 IndexError가 발생하게 됩니다. 따라서 그 경우에 None 값을 반환하도록 구문을 설정하였습니다.  

```python
BASE_URL2 = 'https://api.themoviedb.org/3'
path2 = '/movie/'+ str(id_data) + '/recommendations'
parameter2 = {
    'api_key': '1d782b494774c8b795a68a320100ebdd',
    'language': 'KO'}
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter2 내의 값은 path2값에 따라 달라집니다. 

path2 의 주소에 id값을 넣어야하기에 위의 코드에서 받아온 `id_data` 를 string 형태로 바꿔 안에 집어넣었습니다.

```python
response2 = requests.get(BASE_URL2 + path2, params = parameter2).json()
datas2 = response2['results']
recmd_movie_title = []
for data in datas2:
    recmd_movie_title.append(data['title'])

return recmd_movie_title
```

`response2` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

`datas2` 를 `response2 ` dictionary 안의 'results' key 의 value값들로 정의합니다. 영화 정보가 담긴 list값이 될 것입니다.

`recmd_movie_title` 을 리스트의 형태로 정의합니다. 추천 영화의 제목들을 저장할 예정입니다.

`datas2` 리스트 내의 값들에 대해 반복문을 정의합니다.

`data`  dictionary의 'title' 을 key로 가지는 value값들을 `recmd_movie_title` 에 추가합니다.

`recmd_movie_title` 을 반환합니다.

#### 피드백

- path 주소 사이에 변수를 집어넣어야해서 앞/뒤를 끊어 + 형태로 집어넣었다.
- None값 출력하기 위하여 try-except 방식을 사용하였는데 현재 내 코드에서 다른 에러도 발생할 수 있는 지 궁금하다.

---

---

### E. 배우, 감독 리스트 출력

#### 전체 코드

```python
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    # 1. URL 및 요청변수 설정  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    parameter = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'query': {title},
        'region': 'KR',
        'language': 'KO'}
    
    # 2. 요청 보낸 결과 저장
    response = requests.get(BASE_URL + path, params = parameter).json()
    try:
       id_data = response['results'][0]['id']
    except IndexError:
        return None 
    

    BASE_URL2 = 'https://api.themoviedb.org/3'
    path2 = '/movie/' + str(id_data) + '/credits'
    parameter2 = {
        'api_key': '1d782b494774c8b795a68a320100ebdd',
        'language': 'KO'}
    
    response2 = requests.get(BASE_URL2 + path2, params = parameter2).json()
    datas_cast = response2['cast']
    datas_crew = response2['crew']
    cast_id_under_10 = []
    dpt_direc = []
    for data_cast in datas_cast:
        if data_cast['cast_id'] < 10:
            cast_id_under_10.append(data_cast['name'])
    for data_crew in datas_crew:
        if data_crew['department'] == 'Directing':
            dpt_direc.append(data_crew['name'])
    
    cast_crew_dic = {'cast': cast_id_under_10, 'crew': dpt_direc}

    return cast_crew_dic
```



#### 코드 분석

```python
def credits(title):
    pass 
```

`credits` 함수를 정의합니다. 이 함수는 `title` 을 변수로 갖습니다.

```python
BASE_URL = 'https://api.themoviedb.org/3'
path = '/search/movie'
parameter = {
    'api_key': '1d782b494774c8b795a68a320100ebdd',
    'query': {title},
    'region': 'KR',
    'language': 'KO'}
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter 내의 값은 path값에 따라 달라집니다. 

```python
response = requests.get(BASE_URL + path, params = parameter).json()
try:
    id_data = response['results'][0]['id']
except IndexError:
    return None 
```

`response` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

올바르지 않은 영화 제목으로 검색하여 id가 존재하지 않는 경우 None 을 출력하기 위한 try-except 문입니다. 정상적인 영화 제목이 검색된다면 `response['results']` 값이 존재하여 index 0번을 찾아가는 `response['results'][0]` 값이 존재하겠지만 올바르지 않은 제목으로 검색한다면 response 값 자체가 존재하지 않아 IndexError가 발생하게 됩니다. 따라서 그 경우에 None 값을 반환하도록 구문을 설정하였습니다.  

```python
BASE_URL2 = 'https://api.themoviedb.org/3'
path2 = '/movie/' + str(id_data) + '/credits'
parameter2 = {
    'api_key': '1d782b494774c8b795a68a320100ebdd',
    'language': 'KO'}
```

`request.get()` 괄호 안에 들어갈 주소를 미리 입력합니다. parameter2 내의 값은 path2값에 따라 달라집니다. 

path2 의 주소에 id값을 넣어야하기에 위의 코드에서 받아온 `id_data` 를 string 형태로 바꿔 안에 집어넣었습니다.

```python
response2 = requests.get(BASE_URL2 + path2, params = parameter2).json()
datas_cast = response2['cast']
datas_crew = response2['crew']
cast_id_under_10 = []
dpt_direc = []
for data_cast in datas_cast:
    if data_cast['cast_id'] < 10:
        cast_id_under_10.append(data_cast['name'])
for data_crew in datas_crew:
    if data_crew['department'] == 'Directing':
        dpt_direc.append(data_crew['name'])

cast_crew_dic = {'cast': cast_id_under_10, 'crew': dpt_direc}

return cast_crew_dic
```

`response2` 는 `request.get()` 으로 가져온 정보를 json파일 형식으로 하여 정의됩니다. Python에서는 dictionary형태로 보일 것입니다. 

`datas_cast` 를 `response2` dictionary 의 'cast' key 값을 가진 value로 정의합니다 list형태가 됩니다.

`datas_crew` 를 `response2` dictionary 의 'cast' key 값을 가진 value로 정의합니다 list형태가 됩니다.

`cast_id_under_10` 을 list의 형태로 정의합니다. id 값이 10보다 작은 cast들의 이름이 들어갈 예정입니다.

`dpt_direc` 을 list의 형태로 정의합니다. department 가 Directing 인 crew들의 이름이 들어갈 예정입니다.

`datas_cast` 리스트 내의 값들에 대해 반복문을 정의합니다.

만약 `data_cast` dictionary의 'cast_id' key를 가진 value값이 10보다 작을 경우 `cast_id_under_10` 에 `data_cast` dictionary의 'name' key를 가진 value값을 추가합니다.

 `datas_crew` 리스트 내의 값들에 대해 반복문을 정의합니다.

만약 `data_crew` dictionary의 'department' key를 가진 value값이 'Directing' 일 경우 `dot_direc` 에 `data_crew` dictionary의 'name' key를 가진 value값을 추가합니다.

`cast_crew_dic` 을 key값이 'cast', 'crew', value값이 cast_id_under_10, dpt_direc 인 directory로 정의합니다.

`cast_crew_dic` 을 반환합니다. 

#### 피드백

- 무턱대로 'results' 값 사용할 수도 있었지만 json파일 형태를 보고 진행하여 그런 사고를 막을 수 있었다.

---

---

## 총평

이번에는 주어진 json파일을 사용하는 것이 아닌 직접 정보를 끌어와서 json파일로 정의한 후 그 값을 끌어오는 방식으로 프로젝트를 진행했습니다. 실시간으로 변동하는 정보를 끌어올 수도 있으므로 실생활에서 더욱 그 사용성이 높을 것으로 보입니다. 

requests 모듈만 있다면 어느 사이트던지 api 를 활용하여 정보를 끌어올 수 있게 되었습니다. 이제 이 끌어온 데이터를 사용자에게 예쁘게 보이게 하는 것을 배우게 될 텐데 어떤 식으로 이 데이터를 꾸며 프론트로 내보낼 수 있을지 기대가 됩니다.