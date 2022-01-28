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

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
