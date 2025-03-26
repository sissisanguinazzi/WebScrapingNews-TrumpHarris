import requests


def fetch_articles(api_key, section="us-news/kamala-harris", page_size=50):
    """
    Fetch articles from the Guardian API for a specific section
    Parameters:
    - api_key (str): The API key for the Guardian API
    - section (str): The section to fetch articles from
    - page_size (int): The number of articles to fetch
    Returns:
    - list: A list of article URLs
    """
    # Construct the url
    url = f"https://content.guardianapis.com/{section}?api-key={api_key}&show-fields=all&page-size={page_size}"

    # Make the request to the API
    response = requests.get(url)
    # Parse JSON data returned by the API
    data = response.json()

    article_list_harris = []

    # Extract article URLs
    if "response" in data and "results" in data["response"]:
        for article in data["response"]["results"][:20]:
            # Append URLs to the empty list
            article_list_harris.append(article['webUrl'])
        print(f"Retrieved {len(article_list_harris)} articles")
    else:
        print("No articles found.")

    return article_list_harris