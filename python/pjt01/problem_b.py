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