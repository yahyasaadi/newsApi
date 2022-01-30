from app import app
import urllib.request, json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']
main_url = app.config['NEWS_API_BASE_URL']


# function to get the new
def get_news():
    
    index_url = main_url.format(api_key)

    with urllib.request.urlopen(index_url) as url:
        get_news_data = url.read()
        news_reponse = json.loads(get_news_data)

        news_results = None

        if news_reponse['sources']:
            news_results_list = news_reponse['sources']
            news_results = process_results(news_results_list)

    return news_results



def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news article details
    Returns :
        news_results: A list of news objs
    '''
    news_results = []

    for new_article in news_list:
        id = new_article.get('id')
        name = new_article.get('name')
        url = new_article.get('url')
        category = new_article.get('category')
        country = new_article.get('country')

    
        news_obj = News(id,name,url,category,country)
        news_results.append(news_obj)

    return news_results
