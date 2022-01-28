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

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
