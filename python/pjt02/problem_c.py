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
                if data not in vt_avg_5_movie_list:
                    vt_avg_5_movie_list.append(data)
                else:
                    continue

    return vt_avg_5_movie_list

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
