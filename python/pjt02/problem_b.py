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
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
