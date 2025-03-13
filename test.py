from variables import variable_store
import requests
import pandas as pd
import datetime
from database_layer import process_articles

#url = f"https://newsdata.io/api/1/news?apikey=pub_660057b9d6efb16021673be7617c298eb5832&q=octopus%20energy%20OR%20edf%20OR%20British%20gas%20OR%20Scottish%20power%20OR%20Ovo "
#response = requests.get(url)
#data = response.json()
#print(data)

#datetime.datetime.strftime(data["pubDate"],"%Y-%m-%d").strftime("%d-%m-%Y")

#url =  f"https://newsdata.io/api/1/latest?apikey=pub_660057b9d6efb16021673be7617c298eb5832&q=cryptocurrency&from_date=2024-10-30&to_date=2024-10-30"

df = process_articles()
print(df)