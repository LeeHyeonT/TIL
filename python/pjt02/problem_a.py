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

# if __name__ == '__main__':
#     """
#     popular 영화목록의 개수 출력.
#     """
print(popular_count())
    # => 20
