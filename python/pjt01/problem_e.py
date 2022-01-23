import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    month_title_list = []
    for i in range(len(movies)):

        movie_json = open('data/movies/' + str(movies[i]["id"]) + '.json',encoding = 'UTF8')
        movie_list = json.load(movie_json)
        
        month_title_list.append((movie_list['release_date'].split('-')[1],movie_list['title']))
  
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