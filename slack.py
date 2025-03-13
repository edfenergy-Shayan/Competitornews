import requests
import pandas as pd
from database_layer import process_articles
import json
import itertools
import datetime

def slack_output(): 
    url = 'https://hooks.slack.com/services/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'
    df = process_articles()
    #df["pubDate"] = df["pubDate"].apply(lambda x: datetime.datetime.strftime(x, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M"))
    df["pubDate"] = df["pubDate"].apply(lambda x: x.strftime("%d-%m-%Y %H:%M"))

    
    

    block = [
            [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": row['title']
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Read Article",
                            "emoji": True
                        },
                        "value": "click_me_123",
                        "url": row["link"],
                        "action_id": "button-action",
                        "style": "primary"
                    }
                },
                {
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": f"Published: {row["pubDate"]}",
					"emoji": True
				}
			]
		},
        {
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": f"Source: {row["source_id"]}",
					"emoji": True
				}
			]
		},
                
                {
                    "type": "divider"
                }
            ]
            for index, row in df.iterrows()
        ]
    
    block = list(itertools.chain.from_iterable(block)) # chains the lists together

# block for heading
    block2 =   [
		{
			"type": "rich_text",
			"elements": [
				{
					"type": "rich_text_section",
					"elements": [
						{
							"type": "emoji",
							"name": "zap",
							"unicode": "26a1"
						},
						{
							"type": "text",
							"text": "Energy Market Updates",
							"style": {
								"bold": True
							}
						},
						{
							"type": "emoji",
							"name": "zap",
							"unicode": "26a1"
						}
					]
				}
			]
		}
	]

    payload = {"blocks": block2 + block}
    payload_json = json.dumps(payload)
    response = requests.post(url, json=payload, verify=False)
    print(f"Response Status: {response.status_code}")
    print(f"Response Status: {response.text}")
    print(payload)

slack_output()

