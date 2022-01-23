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