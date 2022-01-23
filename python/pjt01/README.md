[toc]

# Python을 활용한 데이터 수집 1



## 1. 목표

- Python 기본 문법 실습
- 파일 입출력에 대한 이해
- 데이터 구조에 대한 분석과 이해
- 데이터를 가공하고 JSON 형태로 저장

## 2. 준비사항

1) TMDB API

   - 평점 순 영화정보 API 서비스
   - 장르 리스트 정보 API 서비스
   - 영화 상세정보 API 서비스
2) 개발언어/프로그램
   - Python 3.9 이상
3) 필수 라이브러리
   - Json

---

## 3. 요구사항

커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 추출해 나가는 과정을 진행합니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다.

### A. 제공되는 영화 데이터의 주요내용 수집

#### 1) 코드

```python
import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    new_arrange = {'id': movie['id'], 'title': movie['title'], 
    'poster_path': movie['poster_path'], 'vote_average': movie['vote_average'], 
    'overview': movie['overview'], 'genre_ids': movie['genre_ids']}
    return new_arrange


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```



#### 2) 코드분석

```python
import json
from pprint import pprint
```

json 형식의 파일을 끌어옵니다. 코드 내부에서 json파일을 끌어다 쓸 수 있게 됩니다.

pprint라는 내부 함수를 끌어옵니다. pprint 함수를 통해 좀 더 정갈한 print가 가능해집니다.

```python
def movie_info(movie):
```

movie_info 라는 함수를 정의합니다. 이 함수는 movie를 인자로 갖습니다. 후에 기술할 내용 덕분에  movie.json 내부에 존재하는 데이터를 인자로 활용하게 됩니다.

```
 new_arrange = {'id': movie['id'], 'title': movie['title'], 
    'poster_path': movie['poster_path'], 'vote_average': movie['vote_average'], 
    'overview': movie['overview'], 'genre_ids': movie['genre_ids']}
    return new_arrange
```

movie.json  내 데이터 안에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져와야하기에 dictionary형태인 movie.json 을 이용하여  필요한 값들을 키 값을 이용하여 끌어왔습니다. 

끌어온 값들을 통해 새로운 dictionary를 만들고 그것의 이름을 new_arrange라 했습니다.

새롭게 정의된 new_arrange값을 반환합니다.

```python
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```

movie.json 파일을 python 내부에서 활용하기위해 사용한 코드입니다. 

`movie_dict`를` movie_info` 함수의 argument로 사용했는데 `movie_dict`는 movie.json파일 내부의 데이터를 끌어온다고 정의했기에 `movie_dict` 값을 통해 `movie_info` 함수 내부에서 movie.json 의 데이터를 인자로 활용할 수 있게 됩니다.

#### 3) 피드백

- json 파일을 끌어오는 과정 및 코드를 알 수 있었습니다.
- `new_arrange` 의 key값을 텍스트로만 설정할 수 있는지, 아니면 코드로 구현할 수 있는지 궁금해집니다.



### B. 제공되는 영화 데이터의 주요내용 수정

#### 1) 코드

```python
import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    genre_name_list = [] 
    for k in range(2):

        movies_genres_in_num = movie['genre_ids'][k]

        for n in range(len(genres)):
            
            if genres[n]['id'] == movies_genres_in_num:
                genre_name_list.append(genres[n]['name'])
            else:
                continue

    movie['genre_ids'] = genre_name_list
    new_arrange_2 = {'id': movie['id'], 'title': movie['title'], 
    'poster_path': movie['poster_path'], 'vote_average': movie['vote_average'], 
    'overview': movie['overview'], 'genre_names': movie['genre_ids']}  
    
    return new_arrange_2
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```



#### 2) 코드분석

```
def movie_info(movie, genres):
```

movie_info라는 함수를 정의합니다. A번과 달리 인자가 두 개입니다. 

A번과 마찬가지로 movie.json 데이터와 genres.json 데이터를 사용합니다.

```python
genre_name_list = [] 
    for k in range(2):

        movies_genres_in_num = movie['genre_ids'][k]

        for n in range(len(genres)):
            
            if genres[n]['id'] == movies_genres_in_num:
                genre_name_list.append(genres[n]['name'])
```

`genre_name_list` 를 list형태로 정의합니다. `genre_name_list` 에는 genre_id 값에 대응하는 genre_name 값이 들어갈 예정입니다.

앞서 본 movie.json 내부에 genre_ids 값이 2개였기에 2번 돌아가는 for문을 생성합니다. 이 for문을 통해 genre_ids 값들을 하나하나 꺼내어 사용하게 될 것입니다. 하나하나 꺼낸 id 값을 `movies_genres_in_num` 이라 정의합니다.

다음 for문은 id 값에 맞는 name값을 찾는 과정입니다. genres.json 데이터 전체를 돌면서 비교해야하기때문에genre.json 데이터의 길이만큼 for 반복문을 시행합니다.

만약 genres.json 데이터의 id값과 `movies_genres_in_num` 값과 일치한다면 `genre_name_list` 에 id값에 대응하는 name값을 추가합니다. 이 과정을 총 2번 시행하기에 `genre_name_list` 에는 두 개의 name값이 추가될 것입니다. 

```python
movie['genre_ids'] = genre_name_list
    new_arrange_2 = {'id': movie['id'], 'title': movie['title'], 
    'poster_path': movie['poster_path'], 'vote_average': movie['vote_average'], 
    'overview': movie['overview'], 'genre_names': movie['genre_ids']}  
    
    return new_arrange_2 
```

genre_ids 값을 앞서 구한 `genre_name_list` 값으로 대체합니다. 

A번과 같은 형태의 새로운 dictionary 를 생성하고 그 이름을 new_arrange_2 라 명명했습니다. 

변경사항으론  genre_ids 였던 key값을 genre_names 로 변경했습니다.

생성된 `new_arrange_2` 값을 반환합니다.

#### 3) 피드백

- 두 개의 json 파일을 받아 쓸 수 있다는 것이 신기했습니다.
- 각각의 id에 해당하는 name 값을 찾아 나서기 위해 for 반복문 두 번을 사용했는데 더 깔끔하게 줄일 수는 없을지 궁금합니다.



### C. 다중 데이터 분석 및 수정

#### 1) 코드

```python
import json
from pprint import pprint

def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    genre_ids_list = []
    genre_name_list_bundle = []
    
    for i in range(len(movies)):

        genre_name = []
        genre_ids_list = movies[i]['genre_ids']

        for l in range(len(genre_ids_list)):
            movies_genres_in_num = movies[i]['genre_ids'][l]
            
            for n in range(len(genres)):
                if genres[n]['id'] == movies_genres_in_num:
                    genre_name.append(genres[n]['name'])
                   
                
        genre_name_list_bundle = genre_name
               
        movies[i]['genre_ids'] = genre_name_list_bundle  
             
        new_arrange_2 = {'id': movies[i]['id'], 'title': movies[i]['title'], 
        'poster_path': movies[i]['poster_path'], 'vote_average': movies[i]['vote_average'], 
        'overview': movies[i]['overview'], 'genre_names': movies[i]['genre_ids']}  
        
        movies_list.append([new_arrange_2])
        
    return movies_list

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```



#### 2) 코드 분석

```python
def movie_info(movies, genres):
```

movie_info 함수를 정의합니다. movies.json 데이터와 genres.json 데이터를 이용합니다.

```python
genre_ids_list = []
genre_name_list_bundle = []
```

`genre_ids_list` 와 `genre_name_list_bundle` 을 list 형태로 정의합니다. `genre_ids_list` 에는 movie들의 id list, `genre_name_list_bundle` 에는 movie들의 name list가 들어갈 예정입니다.

```python
for i in range(len(movies)):

    genre_name = []
    genre_ids_list = movies[i]['genre_ids']

    for l in range(len(genre_ids_list)):
        movies_genres_in_num = movies[i]['genre_ids'][l]

        for n in range(len(genres)):
            if genres[n]['id'] == movies_genres_in_num:
                genre_name.append(genres[n]['name'])


    genre_name_list_bundle = genre_name
        
# B번 코드와 비교
    for k in range(2):

            movies_genres_in_num = movie['genre_ids'][k]

            for n in range(len(genres)):

                if genres[n]['id'] == movies_genres_in_num:
                    genre_name_list.append(genres[n]['name'])
```

총 20개의 movie가 있기 때문에 B번에서 작성한 코드를 movies.json 데이터 길이만큼 반복시켜야합니다. 따라서 for 반복문을 사용합니다.

**`genre_name` 을 list 형태로 정의합니다. 반복문 안에서 `genre_name` 을 빈 list형태로 정의한 것은 매우 중요합니다. 후에 기술하겠지만 `genre_name` 값은 계속 어떠한 값을 더하여 받게 될텐데 반복의 시작점에서 내부의 값을 reset시켜줘야 필요한 값을 얻을 수 있게 됩니다. **

B번에서는 1개의 movie에 해당하는 2개의 id가 존재했지만 C번에는 총 20개의 movie에 해당하는 서로 다른 길이의 id값이 존재하기에  for 반복문을 실행할 때 그 범위를 각각의 genre id 의 길이로 설정했습니다.

 B번에서는 1개의 movie만 존재했지만 C번에는 총 20개의 movie가 존재하기에 반복문을 돌면서 그 때마다 필요한 genre_id값을 `movies_genres_in_num` 에 저장합니다.

이후 과정은 B번과 동일합니다.

```python
movies[i]['genre_ids'] = genre_name_list_bundle  
             
        new_arrange_2 = {'id': movies[i]['id'], 'title': movies[i]['title'], 
        'poster_path': movies[i]['poster_path'], 'vote_average': movies[i]['vote_average'], 
        'overview': movies[i]['overview'], 'genre_names': movies[i]['genre_ids']}  
        
        movies_list.append([new_arrange_2])
        
    return movies_list

# B번 코드와 비교
movie['genre_ids'] = genre_name_list
    new_arrange_2 = {'id': movie['id'], 'title': movie['title'], 
    'poster_path': movie['poster_path'], 'vote_average': movie['vote_average'], 
    'overview': movie['overview'], 'genre_names': movie['genre_ids']}  
    
    return new_arrange_2
```

for 반복문을 통해 반복하는 것을 제외하고는 B번과 C번의 형태가 매우 흡사합니다. 불러오는 값의 차이(movie.json / movies.json) , 그에 따른 index값 설정 정도만 다르다고 할 수 있습니다.

과정을 모두 끝내고 `new_arrange_2` 를 반환합니다. 

#### 3) 피드백

- `genre_name` 값을 초기화시키는 걸 너무 늦게 알아차려 시간 소모가 너무 심했습니다. 머리로만 하려고 하니 잘 안 됐던 것 같아 앞으로는 손으로 써 가며 알고리즘을 구상 후 코딩을 해야겠습니다.
- 처음 완성시킨 코드에는 for문이 지금보다 2개가 더 있었습니다. 필요없는 dummy data를 많이 생성한 것이죠. 코드를 보고 보고 또 보면서 필요없는 부분을 잘라낼 수 있었습니다.



### D. 알고리즘을 통한 데이터 출력

#### 1) 코드

```python
import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    revenue_title_list = []
    revenue_list = []
    for i in range(len(movies)):

        movie_json = open('data/movies/' + str(movies[i]["id"]) + '.json',encoding = 'UTF8')
        movie_list = json.load(movie_json)
        
        revenue_title_list.append((movie_list['revenue'],movie_list['title']))
        revenue_list.append(movie_list['revenue'])
    
    for k in range(len(movies)):
        if revenue_title_list[k][0] == max(revenue_list):
            return revenue_title_list[k][1]
        
    
    # if movie_list['budget'] == budget_max:
    #     budget_max_movie = 
    return movie_list['budget']

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```



#### 2) 코드 분석

```
def max_revenue(movies):
```

max_revenue 라는 함수를 정의합니다. movies.json 데이터를 활용하게 됩니다.

```python
revenue_title_list = []
revenue_list = []
```

`revenue_title_list`를 리스트 형태로 정의합니다.  각 movie의 revenue 와  title값이 tuple형태로 묶여 list로 저장할 예정입니다.

`revenue_list` 를 리스트 형태로 정의합니다. 각 movie의 revenue값을 list로 저장할 예정입니다.

```python
for i in range(len(movies)):

        movie_json = open('data/movies/' + str(movies[i]["id"]) + '.json',encoding = 'UTF8')
        movie_list = json.load(movie_json)
        
        revenue_title_list.append((movie_list['revenue'],movie_list['title']))
        revenue_list.append(movie_list['revenue'])
```

movie 갯수만큼 for 반북문을 실행합니다.

movies 폴더 내부에 있는 json파일을 이용해야합니다. movies 폴더 내부에 있는 json파일들의 이름은 각 movie의 id에 해당하기 때문에 movies.json 데이터의 id값을 활용합니다. 또한 파일 명은 integer값이 아닌 string값이기에 str 함수를 사용하여 파일명을 string형태로 바꿔줍니다.

`revenue_title_list` 에 각 movie의 id에 해당하는 json파일에서 revenue 값과 title값을 tuple형태로 묶은 후 그 값을 반복문을 통해 차례로 저장합니다. tuple 로 revenue 값과 title값을 묶은 이유는 후에 title값을 사용해야하기 때문입니다.

`revenue_list` 에 각 movie의 id에 해당하는 json파일에서 revenue값을 반복문을 통해 차례로 저정합니다.

```python
for k in range(len(movies)):
        if revenue_title_list[k][0] == max(revenue_list):
            return revenue_title_list[k][1]
```

movie 갯수만큼 for 반복문을 실행합니다.

앞서 저장한 `revenue_title_list` 값에서 index 0 에 해당하는 revenue 값이 앞서 저장한 `revenue_list` 값들의 최댓값이라면 `revenue_title_list` 값에서 index 1 에 해당하는 title값을 반환합니다. 

이 과정을 통해 revenue가 가장 큰 movie의 title값을 반환할 수 있습니다.

#### 3) 피드백

- revenue값을 비교하는 문제이지만 결국 반환해야할 것은 title값이기에 두 개의 값을 묶어서 tuple형태로 저장하는 것이 효율적이였습니다. 스스로 생각하지 못한 방법이라 아쉽습니다.
- json파일을 불러오기위해 파일명을 변수를 이용해서 작성하는 과정에서 시간을 많이 소모하였습니다. str값으로 변환하는 것, 파일 경로 설정하는 것, encoding 값 넣는 것을 좀 더 신경써야겠습니다.



### E. 알고리즘을 통한 데이터 출력

#### 1) 코드

```python
import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    month_title_list = []
    month_list = []
    for i in range(len(movies)):

        movie_json = open('data/movies/' + str(movies[i]["id"]) + '.json',encoding = 'UTF8')
        movie_list = json.load(movie_json)
        
        month_title_list.append((movie_list['release_date'].split('-')[1],movie_list['title']))
        month_list.append(movie_list['release_date'].split('-')[1])
  
    movies_12_list = []
    for k in range(len(movies)):
        if month_title_list[k][0] == '12':
            movies_12_list.append(month_title_list[k][1])
            
    return movies_12_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```



#### 2) 코드 분석

```python
def dec_movies(movies):
```

dec_movies 라는 함수를 정의합니다. movies.json 데이터를 활용합니다.

```python
month_title_list = []
for i in range(len(movies)):

    movie_json = open('data/movies/' + str(movies[i]["id"]) + '.json',encoding = 'UTF8')
    movie_list = json.load(movie_json)

    month_title_list.append((movie_list['release_date'].split('-')[1],movie_list['title']))
```

`month_title_list` 를 리스트의 형태로 정의합니다. movie의 방영 달과 movie title을 tuple형태로 묶어 저장할 예정입니다.  

movie 갯수만큼 for 반복문을 실행합니다.

D번과 동일한 방법으로 json파일을 불러옵니다.

`month_title_list` 에 데이터를 저장합니다. release_date 값은 '2022-01-23' 의 형태로 이루어져있는데 이 값을 split함수를 사용하여 (2022, 01, 23) 이런 식으로 값을 쪼갤 수 있습니다. 쪼갠 값에서 index 1번에 해당하는 것이 달 이기에 그것을 가져옵니다. 이렇게 해서 구한 달 값과 title값을 tuple 형태로 저장합니다. 

```python
movies_12_list = []
for k in range(len(movies)):
    if month_title_list[k][0] == '12':
        movies_12_list.append(month_title_list[k][1])
            
return movies_12_list
```

`movies_12_list`를 리스트의 형태로 정의합니다. 달 의 값이 12 인 movie의 title을 저장할 예정입니다.

movie 갯수만큼 for 반복문을 실행합니다.

`month_title_list` 내부 tuple값에서 index 0번에 해당하는 값이 달 값이기에 그 값이 12라면 내부 tuple값에서 index 1번에 해당하는 값인 title값을 `movies_12_list` 에 저장합니다.

모든 과정을 기치고 나온 `movies_12_list` 를 반환합니다.

#### 3) 피드백

- split 함수를 이용하여 값을 쪼갠 후 필요한 값을 꺼내어 쓸 수 있었습니다.
- 처음 코드를 작성할 때 불필요한 값까지 정의하여 저장했는데 그런 실수를 줄일 필요가 있겠습니다.

---

---

## 총평

- 반복문과 조건문을 활용하여 필요한 데이터를 뽑아 사용해보았습니다. 반복문 내에 반복문을 사용할 시 변수 설정을 함에 있어 주의가 요구되었습니다. 
- json 파일을 끌어와 그 파일의 내부 데이터를 활용할 수 있다는 점이 흥미로웠습니다. 
- 시간 내에 완성하지 못해 아쉽습니다. 돌이켜보면 작은 실수 하나를 발견하지 못하여 시간을 오래 끌게 된 것이 패착입니다. 아직 코드를 짜는 데 있어 허술한 부분이 많다는 것을 보여준다 생각합니다.
- 같은 결과가 나오는 코드라도 그 형태가 다를 수 있음을, 초안 완성 후 다듬을 수 있는 부분은 최대한 다듬는 것이 좋다고 생각합니다. 저 같은 경우 초안에서 for문을 너무 많이 사용하여 합칠 수 있는 부분은 합쳐보는 시간을 가졌습니다.

