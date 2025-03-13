import pandas as pd
from database_layer import process_articles
from api_connector import fetch_articles

def save_to_csv():
    dataframe = process_articles()

    try:
        # Save DataFrame to CSV
        dataframe.to_csv('output.csv', index=False)
        print("Data saved successfully")
    except Exception as e:
        print("An error occurred")

save_to_csv()