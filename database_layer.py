import pandas as pd
from api_connector import fetch_articles
from variables import variable_store
import datetime

date_str = variable_store["todays_date"]
date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

def process_articles():
    """
    Process and clean the list of articles.
        
    Returns:
        pd.DataFrame: DataFrame containing unique articles with their title and link.
    """
    articles = fetch_articles()
    if articles:
        # Normalize the JSON data into a DataFrame (no need for "results" since the data is already flat)
        article_df = pd.json_normalize(articles)
        
        # Select only the 'title' and 'link' columns
        dataframe = article_df[["title", "link","pubDate","source_id"]]

        dataframe['pubDate'] = pd.to_datetime(dataframe['pubDate'])
        dataframe = dataframe[dataframe["pubDate"].dt.date == date]

        # Remove duplicates if any (optional)
        dataframe = dataframe.drop_duplicates(subset="title",keep='first')
        
        print(f"Total unique articles fetched: {len(dataframe)}")
        return dataframe
    else:
        print("No articles to process.")
        return pd.DataFrame()

    






