from textblob import TextBlob
import nltk
nltk.download('punkt')
from newspaper import Article


def article(url):
    """
    Fetch the content of an article from a given URL
    Parameters:
    - url (str): The URL of the article to fetch
    Returns:
    - tuple: A tuple containing the article's text and title
    """
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.text, article.title


def sentiment_analysis(article_text):
    """
    Perform sentiment analysis on the article text
    Parameters:
    - article_text (str): The text of the article to analyze
    Returns:
    - tuple: A tuple containing the polarity, subjectivity, and their classifications
    """
    # Perform sentiment analysis on the entire article text
    news_article = TextBlob(article_text)

    # Get the overall polarity and subjectivity for the entire article
    polarity = news_article.sentiment.polarity
    subjectivity = news_article.sentiment.subjectivity

    # Classify the polarity and subjectivity based on calculated values
    polarity_class = calculate_sentiment(polarity, "polarity")
    subjectivity_class = calculate_sentiment(subjectivity, "subjectivity")

    return polarity, subjectivity, polarity_class, subjectivity_class


def calculate_sentiment(value, type):
    """
    Classify the polarity or subjectivity value into categories
    Parameters:
    - value (float): The polarity or subjectivity value to classify
    - type (str): The type of value ('polarity' or 'subjectivity')
    Returns:
    - str: The classification label for the polarity or subjectivity value
    """
    if type == "polarity":
        if value > 0.75:
            return "Extremely positive"
        elif value > 0.5:
            return "Significantly positive"
        elif value > 0.3:
            return "Fairly positive"
        elif value > 0.1:
            return "Slightly positive"
        elif value < -0.75:
            return "Extremely negative"
        elif value < -0.5:
            return "Significantly negative"
        elif value < -0.3:
            return "Fairly negative"
        elif value < -0.1:
            return "Slightly negative"
        else:
            return "Neutral"
    
    elif type == "subjectivity":
        if value > 0.75:
            return "Extremely subjective"
        elif value > 0.5:
            return "Fairly subjective"
        elif value > 0.3:
            return "Moderately subjective"
        elif value > 0.1:
            return "Slightly subjective"
        else:
            return "Objective"