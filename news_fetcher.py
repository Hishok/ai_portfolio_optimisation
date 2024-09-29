import requests
from config import NEWS_API_KEY

def fetch_news_articles(query):
    """
    Fetches relevant news articles in English for a given query (e.g., ETF tickers) and limits to 5 articles.
    
    Args:
        query (str): ETF ticker symbol or related query.

    Returns:
        list: A list of (title, link) tuples for relevant articles.
    """
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request failed
        articles = response.json().get('articles', [])
        
        news_links = []
        for article in articles:
            # Safely extract title, URL, and language (fallbacks if missing)
            title = article.get('title', 'No title available')
            url = article.get('url', '#')  # Default to '#' if no URL is available
            language = article.get('language', 'unknown')

            # Only include articles that are explicitly in English
            if language == 'en':
                news_links.append((title, url))
        
        return news_links

    except Exception as e:
        print(f"Error fetching news for {query}: {e}")
        return []
