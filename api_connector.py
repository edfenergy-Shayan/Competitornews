from variables import variable_store
import requests
import pandas as pd

def fetch_articles():
    """"function to fetch news articles from the url"""

    url = f"https://newsdata.io/api/1/news?apiKey={variable_store['api_key']}&qintitle={variable_store['query']}&&country=gb"
    
    all_articles = []  # List to store all fetched articles
    
    while url:  # fetching until there's no next page
        response = requests.get(url)
        data = response.json()

        # check if the 'results' key exists in the data
        if data and "results" in data:
            all_articles.extend(data["results"])  # Add the current page's articles to the list
            print(f"fetched {len(data['results'])} articles")

            # Get the nextPage value to construct the next page's URL
            next_page = data.get('nextPage', None)
            if next_page:
                url = f"https://newsdata.io/api/1/news?apiKey={variable_store['api_key']}&q={variable_store['query']}&country=gb&page={next_page}"
            else:
                print("No more pages to fetch.")
                break
        else:
            print("No articles found or error in response.")
            break
    
    return all_articles


