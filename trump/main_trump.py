from .scraping_trump import fetch_articles
from .nlp_trump import sentiment_analysis, article
import os


articles_trump = []

# Retrieve the API key
api_key = os.getenv("API_KEY")

# Check if the API key is available
if not api_key:
    raise ValueError("Error: API key not found. Please set the 'API_KEY' environment variable.")

# Fetch article URLs using the fetch_articles function from the scraping_trump module
article_harris_urls = fetch_articles(api_key)

# Get article content and perform sentiment analysis
for article_url in article_harris_urls:
    article_text, article_title = article(article_url)

    polarity, subjectivity, polarity_class, subjectivity_class = sentiment_analysis(article_text)

    # Store the article details
    articles_trump.append({
        "title": article_title,
        "content": article_text,
        "url": article_url,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "polarity_class": polarity_class,
        "subjectivity_class": subjectivity_class
    })