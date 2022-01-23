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

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))