from . import app
import urllib.request, json

api_key = app.config['NEWS_API_KEY']

index_url = "https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}"

# function to get the new
def get_news():
    
    with urllib.request.urlopen(index_url) as url:
        get_news_data = url.read()
        news_reponse = json.loads(get_news_data)

        news_results = None

        if news_reponse['results']:
            news_results_list = news_reponse['results']
            news_results = process_results(news_results_list)

    return news_results



def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []

    for new_article in news_list:
        id = new_article.get('id')
        name = new_article.get('name')
        url = new_article.get('url')
        category = new_article.get('category')
        country = new_article.get('country')

        # if poster:
        #     movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
        #     movie_results.append(movie_object)

    return news_results
