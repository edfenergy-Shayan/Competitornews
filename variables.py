variable_store = {"api_key": "Your_API_KEY",
                  #"todays_date": datetime.datetime.today().strftime("%Y-%m-%d"),
                  "todays_date": (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
                  "query": "octopus%20energy%20OR%20edf%20OR%20British%20gas%20OR%20Scottish%20power%20OR%20Ovo%20AND%20Energy%20OR%20electricity%20OR%20Tariff%20OR%20Ofgem%20OR%20heat%20OR%20EV"}
