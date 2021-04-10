from newsapi import NewsApiClient
from decouple import config

from news.models import News

newsapi = NewsApiClient(api_key=config('NEWS_API_KEY'))

def get_top_headline():
    """
    Grabs the latest headline from newsapi
    """
    top_headlines = newsapi.get_top_headlines(language='en', page_size=1)
    return top_headlines['articles'][0]


def save_top_news():
    """
    We get the lastest news and save it to our News Model in the Database
    """
    headline = get_top_headline()
    # lets make sure we don't save the same news more than once
    # we are assuming each news has a unique Link
    if not News.objects.filter(url=headline['url']).exists():
        news = News(
            source=headline['source'],
            author=headline['author'],
            title=headline['title'],
            description=headline['description'],
            url=headline['url'],
            image_url=headline['urlToImage'],
            published_at=headline['publishedAt'],
            content=headline['content'],
        )
        news.save()
